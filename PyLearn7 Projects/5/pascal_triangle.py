def pascal_triangle(n):
    list_of_numbers = []
    for i in range(n):
        list_of_numbers.append([1] * (i + 1))

    for i in range(2, n):
        for j in range(1, i):
            list_of_numbers[i][j] = list_of_numbers[i - 1][j - 1] + list_of_numbers[i - 1][j]

    for row in list_of_numbers:
        print(row)


pascal_triangle(int(input("n = ")))
