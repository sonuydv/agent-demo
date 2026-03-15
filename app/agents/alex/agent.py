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


def run_agent(user_id:str,user_message:str):
    # Fetch user chat history
    history = get_chat_history(user_id)

    # Store user message to history
    save_message(user_id,"User",user_message)

    # Build prompt for llm
    prompt = promptBuilder.build(
        history=history,
        message=user_message
    )
    # LLM response reply
    response =  ask_llm(prompt)

    # Save agent reply to user chat history
    save_message(user_id,"assistant",response)
    return response



async def reply(update:Update,context:ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_name = user.username
    user_message = update.message.text
    print(f"User: {user_name} : {user_message}")
    response =  run_agent(user_name,user_message)
    await update.message.reply_text(response)


TELEGRAM_BOT_KEY = os.getenv("TELEGRAM_BOT_TOKEN")
app = ApplicationBuilder().token(TELEGRAM_BOT_KEY).build()

handler = MessageHandler(filters.TEXT & ~filters.COMMAND,reply)
app.add_handler(handler)

print("Bot is running")

app.run_polling()

