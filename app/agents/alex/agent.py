from agents.alex.prompt_builder import PromptBuilder
from agents.alex.chat.chats_sqlite import get_chat_history,save_message
from llm import ask_llm
from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, MessageHandler, filters

import os
from dotenv import load_dotenv


# Load environment keys from .env to process env
load_dotenv()

promptBuilder = PromptBuilder()


def run_agent(chat_id:str,first_name:str,chat_type:str, user_message:str):
    # Fetch user chat history
    history = get_chat_history(chat_id)

    # Store user message to history
    save_message(chat_id, first_name, user_message)

    # Build prompt for llm
    prompt = promptBuilder.build(
        first_name=first_name,
        history=history,
        message=user_message,
        chat_type=chat_type
    )
    # LLM response reply
    response =  ask_llm(prompt)

    # Save agent reply to user chat history
    save_message(chat_id, "assistant", response)
    return response



async def reply(update:Update,context:ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat.id
    chat_type = update.message.chat.type
    user_name = update.message.chat.first_name or update.message.from_user.first_name
    first_name = user_name.partition("_")[0] or "user"
    user_message = update.message.text

    response =  run_agent(chat_id,first_name,chat_type,user_message)
    await update.message.reply_text(response)


TELEGRAM_BOT_KEY = os.getenv("TELEGRAM_BOT_TOKEN")
app = ApplicationBuilder().token(TELEGRAM_BOT_KEY).build()

handler = MessageHandler(filters.TEXT & ~filters.COMMAND,reply)
app.add_handler(handler)

print("Bot is running")

app.run_polling()

