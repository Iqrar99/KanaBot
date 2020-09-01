import os
import telebot
from telebot import types
from dotenv import load_dotenv
from letters import JLetters


load_dotenv()
API = os.getenv("API_KEY")
bot = telebot.TeleBot(API)
jletters = JLetters()
command_sequence = []

@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name

    welcome_message = (
        f"Hello <b>{user_first_name} {user_last_name}</b>! Welcome to <b>KanaBot</b>!\n"
        "KanaBot will help you to memorize Kana letters by giving you some questions.\n"
        "Choose your quiz session:\n"
        "/hiragana - Start hiragana quiz.\n"
        "/katakana - Start katakana quiz.\n"
        "/exam - Start hiragana + katakana quiz.\n\n"    
        "If you need help for all commands list, type /help."
    )

    bot.reply_to(message, welcome_message, parse_mode="HTML")

@bot.message_handler(commands=["help"])
def send_help(message):

    # TODO : Write command lists
    help_message = (
        "<b>KanaBot command lists:</b>\n\n"
        "(COMING SOON)"
    )

    bot.reply_to(message, help_message, parse_mode="HTML")

@bot.message_handler(commands=["hiragana"])
def hiragana_quiz_start(message):

    hiragana_rule = (
        "This is Hiragana quiz. We will give you 2 types of question.\n"
        "Type 1: Romaji to Hiragana\n"
        "Type 2: Hiragana to Romaji\n\n"
        "After you see a question, simply just type the answer in the chat.\n"
        "We strongly recommend to have <b>Japanese keyboard</b> in your phone before "
        "taking this quiz.\n\n"
        "Choose your question type:\n"
        "<b>1</b> or <b>2</b>"
    )
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add("1", "2")
    bot.reply_to(message, hiragana_rule, reply_markup=markup, parse_mode="HTML")


if __name__ == "__main__":
    print("Bot is running")
    bot.polling()
