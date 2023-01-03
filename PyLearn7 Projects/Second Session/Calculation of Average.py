scores = []
for i in range(1000):
    scores.append(input("Grade = "))
    if scores[i] == "exit" or scores[i] == "EXIT" or scores[i] == "Exit":
        scores.pop(-1)
        break
    else:
        continue

# Converting Strings to float numbers
floated_scores = [float(score) for score in scores]

average = sum(floated_scores) / len(floated_scores)
print(f"The Average of {floated_scores} is equal to {round(average, 3)}.")
