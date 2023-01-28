n = int(input("Enter the Length of the Snake: "))
snake = []
for i in range(n):
    if i % 2 == 0:
        snake.append("*")
    else:
        snake.append("#")

print("".join(snake))