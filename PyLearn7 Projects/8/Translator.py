import sys
from playsound import playsound
from gtts import gTTS

words_bank = []


def read_from_file():
    try:
        file = open("translate.txt", "r")
        temp = file.read().split("\n")
        if "" in temp:
            temp.remove("")

        for i in range(0, len(temp), 2):
            my_dict = {"en": temp[i], "fa": temp[i + 1]}
            words_bank.append(my_dict)

        file.close()
    except FileNotFoundError or FileExistsError:
        print("File is not in the Directory.")
        sys.exit()


def playaudio(audio):
    playsound(audio)


def convert_to_audio(text):
    audio = gTTS(text=text, lang='en', tld='co.uk')
    audio.save(f"{text}.mp3")
    playaudio(f"{text}.mp3")


def translate_english_to_persian():
    user_text = input("Enter your English Text: ")
    user_text = user_text.lower()

    user_words = user_text.split(".")
    if "" in user_words:
        user_words.remove("")
    first_result = [item.split(' ') for item in user_words]

    second_result = []

    for element in first_result:
        second_result.append(element)
        second_result.append(["."])

    result_flat = [item for l in second_result for item in l]

    for element in result_flat:
        if "" in result_flat:
            result_flat.remove("")

    output = ""

    for user_word in result_flat:
        for word in words_bank:
            if user_word == word["en"]:
                output = output + word["fa"] + " "
                break
        else:
            output = output + user_word + " "
    print(f"Persian Translation is: {output}")
    convert_to_audio(output)


def translate_persian_to_english():
    user_text = input("Enter your Persian Text: ")
    user_text = user_text.lower()

    user_words = user_text.split(".")
    if "" in user_words:
        user_words.remove("")
    first_result = [item.split(' ') for item in user_words]

    second_result = []

    for element in first_result:
        second_result.append(element)
        second_result.append(["."])

    result_flat = [item for l in second_result for item in l]

    for element in result_flat:
        if "" in result_flat:
            result_flat.remove("")

    output = ""

    for user_word in result_flat:
        for word in words_bank:
            if user_word == word["fa"]:
                output = output + word["en"] + " "
                break
        else:
            output = output + user_word + " "

    print(f"English Translation is: {output}")
    convert_to_audio(output)


def show_menu():
    print("_____________________________________________")
    print("Welcome to my Translator.")
    print("1 - Translate English to Persian")
    print("2 - Translate Persian to English")
    print("3 - Add a new word to the Database")
    print("4 - Exit")
    print("_____________________________________________")


read_from_file()


def add_word():
    proceed = "y"
    while proceed.lower() == "y":
        eng = input("Enter the English Word: ")
        eng = eng.lower()
        for i in range(len(words_bank)):
            if eng in words_bank[i]["en"]:
                print("This Word is in the List.")
                print(words_bank[i]["en"] , ": ", words_bank[i]["fa"])
                break

        else:
            fa = input("Enter the Persian Translation: ")
            fa = fa.lower()
            new_word = {
                "en": eng,
                "fa": fa,
            }
            words_bank.append(new_word)
            proceed = input("Do you want to Proceed(Y/N)? ")

    file = open("translate.txt", "w")
    for i in range(len(words_bank)):
        file.write(f"{words_bank[i]['en']}\n{words_bank[i]['fa']}\n")

    file.close()


while True:

    show_menu()
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            translate_english_to_persian()

        elif choice == 2:
            translate_persian_to_english()

        elif choice == 3:
            add_word()

        elif choice == 4:
            exit(0)
        else:
            print("Enter correct Choice.")
            continue

    except ValueError:
        print("Enter correct Value.")
        continue
