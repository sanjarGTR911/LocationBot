from telegram import Update
from telegram.ext import ContextTypes
from database import save_user_data

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    username = user.username or ""
    full_name = f"{user.first_name or ''} {user.last_name or ''}".strip()

    # Save user silently
    save_user_data(user_id, username, full_name)

    # No response to user
    # Agar xohlasa, admin kanalga yoki logga yozish mumkin
