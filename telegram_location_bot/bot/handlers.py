from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from services.geocoder import get_location_from_address
from asyncio import get_event_loop
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from bot.database import save_user_data
from bot.keyboard import create_reply_keyboard, get_map_links
from bot.database import mark_user_inactive

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        f"👋 Hi {user.first_name}!\n\n"
        "To get started, please *share your location* or *type your address*.\n\n"
        "Need help? Tap ❓ Help\n"
        "Have questions? Tap 📞 Contact Us\n\n"
        "👇 Choose an option below:",
        reply_markup=create_reply_keyboard()
    )
    # Save user to database (basic info)
    save_user_data(
        user_id=user.id,
        username=user.username or "",
        full_name=user.full_name or ""
    )

# Address handler - geocode + location + inline buttons
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    address = update.message.text
    loop = get_event_loop()

    # Get coordinates using geocoding (in background thread)
    location = await loop.run_in_executor(None, get_location_from_address, address)

    if location:
        # Create inline buttons for map and taxi
        keyboard = [
            [InlineKeyboardButton("📍 View on Map",
                url=f"https://yandex.com/maps/?ll={location['lon']},{location['lat']}&z=16")],
            [InlineKeyboardButton("🚕 Order Taxi (Yandex Go)",
                url=f"https://3.redirect.appmetrica.yandex.com/route?end-lat={location['lat']}&end-lon={location['lon']}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send location + buttons
        await update.message.reply_location(latitude=location["lat"], longitude=location["lon"])
        await update.message.reply_text(
            "✅ *Location found!*\nChoose what you'd like to do:",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            "❌ *Location not found.*\nPlease double-check the address and try again.",
            parse_mode="Markdown"
        )

# Help handler
async def handle_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ *Help Information:*\n\n"
        "Just send a location name or address and I'll find it on the map for you.\n"
        "You can also click 'Send My Location' to let me find where you are right now."
        "You can also order a taxi using the links I provide after receiving your location.\n"
        "Let me know if you need more help!",
        parse_mode="Markdown"
    )

async def handle_contact_us(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 *Contact Us:*\n\n"
        "If you need support, feel free to reach out:\n"
        "📧 Email: your_email\n"
        "📱 Phone: your_phone_number",
        parse_mode="Markdown"
    )

async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lat = update.message.location.latitude
    lon = update.message.location.longitude

    # Send location-related buttons (map & taxi links)
    await update.message.reply_text(
        "Here are the map links and options for your location:",
        reply_markup=get_map_links(lat, lon)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge the callback

    if query.data == 'help':
        await handle_help(update, context)
    elif query.data == 'contact':
        await handle_contact_us(update, context)

async def notify_user(context):
    try:
        await context.bot.send_message(chat_id=id, text="Hello again!")
    except Exception as e:
        if "Forbidden" in str(e):  # bot blocked by user
            mark_user_inactive(id)

def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^❓ Help$"), handle_help))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^📞 Contact Us$"), handle_contact_us))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.add_handler(MessageHandler(filters.LOCATION, handle_location))
    app.add_handler(CallbackQueryHandler(button, pattern="^(help|contact)$"))
