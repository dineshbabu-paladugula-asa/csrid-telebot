import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters
from app.settings import TOKEN
from app.states import RATING, FEEDBACK, RECOMMEND
from app.bot import start, rating, feedback, recommend, cancel

def main() -> None:
    """Run the bot."""
    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            RATING: [MessageHandler(filters.TEXT & ~filters.COMMAND, rating)],
            FEEDBACK: [MessageHandler(filters.TEXT & ~filters.COMMAND, feedback)],
            RECOMMEND: [MessageHandler(filters.Regex("^(Yes|No|yes|no)$"), recommend)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    application.run_polling()

if __name__ == "__main__":
    main()
