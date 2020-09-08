import os
import telebot
from telebot import types
from dotenv import load_dotenv
from utils.generator import QuizGenerator
from utils.letters import JLetters


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
        "Type 1: Hiragana to Romaji\n"
        "Type 2: Romaji to Hiragana\n\n"
        "After you see a question, simply just type the answer in the chat.\n"
        # For now, we just use 20 questions. Will add new feature to handle this option in the future
        "There are 20 questions will be shown.\n"
        "We strongly recommend to have <b>Japanese keyboard</b> in your phone before "
        "taking this quiz.\n\n"
        "Choose your question type:\n"
        "<b>1</b> or <b>2</b>"
    )
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add("1", "2")
    msg = bot.reply_to(message, hiragana_rule, reply_markup=markup, parse_mode="HTML")
    bot.register_next_step_handler(msg, process_hiragana_quiz_type)


def process_hiragana_quiz_type(message):
    """Function to handle what quiz type do users want."""

    if message.content_type == "text":
        try:
            quiz_type = int(message.text)
            if quiz_type < 1 or quiz_type > 2:
                msg = bot.reply_to(message, "Quiz type should be 1 or 2 only. Try again.")
                bot.register_next_step_handler(msg, process_hiragana_quiz_type)

            else:
                quiz = QuizGenerator("HIRAGANA", quiz_type)
                msg = bot.reply_to(message, (
                    "HIRAGANA QUIZ START! Ganbatte!\n\n"
                    "Type anything to start.")
                )
                bot.register_next_step_handler(msg, process_quiz_session, quiz)

        except ValueError:
            msg = bot.reply_to(message, "Quiz type should be a number only. Try again, 1 or 2?")
            bot.register_next_step_handler(msg, process_hiragana_quiz_type)

    else:
        msg = bot.reply_to(message, "Input should be in text format. Try again, 1 or 2?")
        bot.register_next_step_handler(msg, process_hiragana_quiz_type)


def process_quiz_session(message, quiz: QuizGenerator):
    cnt = quiz.get_counter()
    quiz.increase_counter()
    print(f"{cnt}, {message.text}")
    if cnt < quiz.QUESTION_LIMIT:
        if cnt > 0:
            # Store user answers for final report purpose
            user_answer = message.text.lower()
            quiz.add_user_answer(user_answer)
            quiz.add_result(user_answer == quiz.get_true_answer(cnt - 1))

        question_now = quiz.get_question(cnt)
        question = (
            f"Question {cnt + 1}\n\n"
            f"{question_now}?"
        )
        msg = bot.send_message(chat_id=message.chat.id, text=question)
        bot.register_next_step_handler(msg, process_quiz_session, quiz)

    else:
        # Store the last answer
        user_answer = message.text.lower()
        quiz.add_user_answer(user_answer)
        quiz.add_result(user_answer == quiz.get_true_answer(cnt - 1))

        result_msg = "Your quiz result!\n\n"
        for idx in range(quiz.QUESTION_LIMIT):
            result_msg += "{}. {} : {} = {}\n".format(
                idx + 1,
                quiz.get_question(idx),
                quiz.get_user_answer(idx),
                "✅" if quiz.get_result(idx) else "❌"
            )
        result_msg += f"\nYour Score: {quiz.get_score()}/{quiz.QUESTION_LIMIT * 10}"
        bot.send_message(chat_id=message.chat.id, text=result_msg)
        bot.send_message(chat_id=message.chat.id, text="Type /start, if you want to try again.")


if __name__ == "__main__":
    print("Bot is running")
    bot.polling()
