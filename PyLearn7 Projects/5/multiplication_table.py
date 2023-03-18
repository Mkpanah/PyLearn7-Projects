def multiplication_table(n:int, m:int):
    print("\t" * (m-3), "Multiplication Table")
    print("x", end="|\t")
    for k in range(1, m + 1):
        print(k, end="\t\t")
    print()
    print("_" * (m*8))
    for i in range(1, n+1):
        print(i, end="|\t")
        for j in range(1, m+1):
            print(i * j, end="\t\t")
        print("\t")


multiplication_table(int(input("rows = ")), int(input("columns = ")))
