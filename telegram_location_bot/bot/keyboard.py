from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram import ReplyKeyboardMarkup, KeyboardButton

def create_reply_keyboard():
    keyboard = [
        [KeyboardButton(text="📍 Send My Location", request_location=True)],
        ['❓ Help', '📞 Contact Us']
    ]
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=False, resize_keyboard=True)


# 🌍 Inline buttons for map links and taxi
def get_map_links(lat, lon):
    yandex_map = f"https://yandex.com/maps/?ll={lon},{lat}&z=16"
    yandex_taxi = f"https://3.redirect.appmetrica.yandex.com/route?end-lat={lat}&end-lon={lon}"

    keyboard = [
        [InlineKeyboardButton("📍 View on Map", url=yandex_map)],
        [InlineKeyboardButton("🚕 Order Taxi (Yandex Go)", url=yandex_taxi)]
    ]
    return InlineKeyboardMarkup(keyboard)


# 📄 Pagination buttons (e.g., for long lists)
def get_pagination_buttons(page: int, max_pages: int):
    keyboard = []

    buttons = []
    if page > 1:
        buttons.append(InlineKeyboardButton("⬅️ Previous", callback_data=f"page_{page - 1}"))
    if page < max_pages:
        buttons.append(InlineKeyboardButton("Next ➡️", callback_data=f"page_{page + 1}"))

    if buttons:
        keyboard.append(buttons)

    return InlineKeyboardMarkup(keyboard)


# ✅/❌ Confirmation buttons (e.g., before sending data)
def create_confirmation_buttons():
    keyboard = [
        [InlineKeyboardButton("✅ Confirm", callback_data='confirm')],
        [InlineKeyboardButton("❌ Cancel", callback_data='cancel')]
    ]
    return InlineKeyboardMarkup(keyboard)


# ❌ Cancel button alone
def create_cancel_button():
    keyboard = [
        [InlineKeyboardButton("❌ Cancel", callback_data='cancel')]
    ]
    return InlineKeyboardMarkup(keyboard)


# ✅ Location shared confirmation
def create_location_shared_confirmation():
    keyboard = [
        [InlineKeyboardButton("📍 Share Another Location", callback_data='share_another')],
        [InlineKeyboardButton("✅ Confirm Location", callback_data='confirm_location')]
    ]
    return InlineKeyboardMarkup(keyboard)
