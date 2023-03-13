import random

capitals_bank = ["warsaw", "madrid", "kabul", "tehran", "baghdad", "beijing", "tokyo", "athena", "cairo", "riadh",
                 "paris", "vienna", "roma", "london", "rio de janeiro", "moscow", "doha", "delhi", "buenos aires"]

capital = random.choice(capitals_bank)
user_mistakes = 0
good_chars = []
bad_chars = []
# print(capital)


while user_mistakes < 6:
    for i in range(len(capital)):
        if capital[i] in good_chars:
            print(capital[i], end=" ")
        else:
            print("_ ", end=" ")

    user_char = input("Please write your Guess: ")
    user_char = user_char.lower()
    if len(user_char) == 1:
        if user_char in capital:
            good_chars.append(user_char)
            # print(True)
            if sorted("".join(set(good_chars))) == sorted([*("".join(set(capital)))]):
                print(f"Selected Capital was {capital} and your Guessed {capital}.")
                print("You Won")
                break
        else:
            bad_chars.append(user_char)
            user_mistakes += 1
            # print(False)
    else:
        print("Please Enter a Valid Character.")

if user_mistakes >= 6:
    print("You Lost")