import os
import telebot
from dotenv import load_dotenv


load_dotenv()
API = os.getenv("API_KEY")
bot = telebot.TeleBot(API)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name

    welcome_message = f"""
    Hello <b>{user_first_name} {user_last_name}</b>! Welcome to <b>KanaBot</b>!
KanaBot will help you to memorize Kana letters by giving you some questions.
Choose your quiz type:
/hiragana - Start hiragana quiz.
/katakana - Start katakana quiz.
/exam - Start hiragana + katakana quiz.

If you need help for all commands list, type /help.
    """

    bot.reply_to(message, welcome_message, parse_mode="HTML")

@bot.message_handler(commands=["help"])
def send_help(message):

    #TODO : Write command lists
    help_message = """
    <b>KanaBot command lists:</b>

(Coming Soon)
    """
    bot.reply_to(message, help_message, parse_mode="HTML")


if __name__ == "__main__":
    print("Bot Running")
    bot.polling()
