bonus_number = 6
numbers = []
for i in range(1000):
    numbers.append(float(input("Throw the Dice: ")))
    if numbers[i] == bonus_number:
        print("You Made it. Throw the dice again.")
        continue
    elif numbers[i] > 6 or numbers[i] < 1:
        print("Import the Correct Number.")
        continue
    else:
        print("Not your Turn Anymore. Give the Dice Away!!")
        break