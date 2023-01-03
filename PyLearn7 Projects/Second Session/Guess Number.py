guess_number = 7
numbers = []
for i in range(1000):
    numbers.append(float(input("Guess a Number: ")))
    if numbers[i] == guess_number:
        break
    else:
        continue

print(f"You Attempted {len(numbers)} times to Correctly Guess the Number.")