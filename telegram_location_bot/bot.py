import logging
from telegram.ext import Application
from bot.handlers import setup_handlers
from config.settings import BOT_TOKEN

# Set up logging to help with debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        # Initialize the application with the token from settings
        app = Application.builder().token(BOT_TOKEN).build()

        # Set up the handlers for commands and messages
        setup_handlers(app)

        # Start polling for new messages
        logger.info("Bot is starting...")
        app.run_polling()

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
