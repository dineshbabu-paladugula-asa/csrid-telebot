from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler
from app.states import RATING, FEEDBACK, RECOMMEND
from app.storage import storage
import logging

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks for rating."""
    await update.message.reply_text(
        "Welcome to our survey!\n\n"
        "How would you rate the product? (1-5)",
    )
    return RATING

async def rating(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the rating and asks for feedback."""
    user_input = update.message.text
    try:
        rating_value = int(user_input)
        if not 1 <= rating_value <= 5:
            raise ValueError
    except ValueError:
        await update.message.reply_text("Please enter a valid number between 1 and 5.")
        return RATING

    storage.update_response(update.message.chat_id, "rating", rating_value)
    
    await update.message.reply_text("Please share your feedback.")
    return FEEDBACK

async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the feedback and asks for recommendation."""
    user_feedback = update.message.text
    storage.update_response(update.message.chat_id, "feedback", user_feedback)

    reply_keyboard = [["Yes", "No"]]
    await update.message.reply_text(
        "Would you recommend this product? (Yes/No)",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True
        ),
    )
    return RECOMMEND

async def recommend(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the recommendation and ends the conversation."""
    user_input = update.message.text
    if user_input.lower() not in ["yes", "no"]:
         await update.message.reply_text("Please answer with Yes or No.")
         return RECOMMEND

    is_recommend = user_input.lower() == "yes"
    storage.update_response(update.message.chat_id, "recommend", is_recommend)

    # Log/Print the final data for verification
    final_data = storage.get_response(update.message.chat_id)
    logger.info(f"Survey completed for {update.message.chat_id}: {final_data}")

    await update.message.reply_text(
        "Thank you for your time!", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    await update.message.reply_text(
        "Survey canceled.", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END
