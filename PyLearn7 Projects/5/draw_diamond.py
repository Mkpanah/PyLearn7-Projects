def draw_diamond(n):
    for i in range(n):
        print(" " * (n - i), "*" * (2 * i + 1))
    for j in reversed(range(n - 1)):
        print(" " * (n - j), "*" * (2 * j + 1))


draw_diamond(int(input("Enter Number of Rows: ")))
