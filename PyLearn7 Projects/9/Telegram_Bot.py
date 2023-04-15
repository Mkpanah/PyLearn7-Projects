import telebot
import random

bot = telebot.TeleBot("6200530885:AAH-Z6tIWf5DMdEeKf9-WLByL-Z9uvdVGCI", parse_mode=None)


def generate_number():
    return random.randint(1, 100)


@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.reply_to(message, f"Hello {message.from_user.first_name}, Welcome to my Bot!")


@bot.message_handler(commands=['game'])
def send_instructions(message):
    bot.reply_to(message, "Welcome to the Guess Number game! I'm thinking of a number between 1 and 100. Try to guess it!")

secret_number = random.randint(1, 100)
@bot.message_handler(func=lambda message: True)
def check_guess(message):
    global secret_number
    try:
        guess = int(message.text)
        if guess < 1 or guess > 100:
            bot.reply_to(message, "Please enter a number between 1 and 100.")
        else:
            if guess == secret_number:
                bot.reply_to(message, "Congratulations! You guessed it right!")
                secret_number = generate_number()
            elif guess < secret_number:
                bot.reply_to(message, "Too low! Try again.")
            else:
                bot.reply_to(message, "Too high! Try again.")
    except ValueError:
        bot.reply_to(message, "Please enter a valid number.")


bot.polling()
