import os  
import logging  
from telegram import Update  
from telegram.ext import Updater, CommandHandler, CallbackContext  

# Настройка логов  
logging.basicConfig(  
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  
    level=logging.INFO  
)  
logger = logging.getLogger(__name__)  

TOKEN = os.getenv("BOT_TOKEN")  

def start(update: Update, context: CallbackContext):  
    update.message.reply_text("🎉 Бот работает!")  

def main():  
    updater = Updater(TOKEN)  
    dp = updater.dispatcher  
    dp.add_handler(CommandHandler("start", start))  

    # Для Railway/Fly.io  
    PORT = int(os.environ.get("PORT", 8080))  
    updater.start_webhook(  
        listen="0.0.0.0",  
        port=PORT,  
        url_path=TOKEN  
    )  
    updater.bot.set_webhook(f"https://your-app-name.railway.app/{TOKEN}")  

    updater.idle()  

if __name__ == "__main__":  
    main()  
