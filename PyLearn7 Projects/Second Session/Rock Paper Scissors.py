import random
options = ["rock", "scissors", "paper"]
my_grade = 0
your_grade = 0

while my_grade < 3 and your_grade < 3:
    my_choice = input("Me: ")
    your_choice = options[random.randint(0, 2)]
    print("You: ", your_choice)
    if my_choice not in options:
        print("Enter Correct Value Dummy!!")
        continue
    elif my_choice == your_choice:
        print("Tied!!")
        print("___________________________")
        continue
    elif (my_choice == "rock" and your_choice == "scissors") or (my_choice == "scissors" and your_choice == "paper") or (my_choice == "paper" and your_choice == "rock"):
        print("Yes I Won")
        my_grade += 1
        print("___________________________")
        continue
    else:
        print("Bummer, You Won !!")
        your_grade += 1
        print("___________________________")
        continue

print(f"The Final Result is ME = {my_grade} and PC = {your_grade}")
if my_grade > your_grade:
    print("I Have Beaten You!!! Lol")
else:
    print("Damn It, You Won!! Lol")