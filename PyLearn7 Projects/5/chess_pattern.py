def chess_pattern(n:int, m:int):
    for i in range(n):
        for j in range(m):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                print("# " , end="")
            else:
                print("* ", end="")
        print()


chess_pattern(int(input("rows = ")), int(input("columns = ")))
