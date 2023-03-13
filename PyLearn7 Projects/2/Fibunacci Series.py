# Import Desired Number of Elements within the series
n = int(input("Number of Elements = "))
# Initialization with Feed Values
scores = [1, 1]

# Handling Improper Input Values
if n == 1:
    print([1])
elif n < 1:
    print("Import Proper Value Dummy !!")
else:
    for i in range(2, n):
        scores.append(scores[i-1] + scores[i-2])
    print(scores)
