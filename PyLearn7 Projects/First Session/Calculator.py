import math
import numpy as np
sign = input("Operation = ")

if sign == "+" or sign =="-" or sign == "*" or sign == "/":
    a = float(input("a = "))
    b = float(input("b = "))
    if sign == "+":
        print(f"The Result is: {a + b}")

    elif sign == "-":
        print(f"The Result is: {a - b}")

    elif sign == "*":
        print(f"The Result is: {a * b}")

    elif sign == "/":
        if b == 0:
            print("Not Proper")
        else:
            print(f"The Result is: {a / b}")

    else:
        print("Undefined Operation.")


else:
    a = float(input("a = "))
    if sign == "sin":
        a *= math.pi / 180
        print(f"The Result is: {round(math.sin(a),3)}")

    elif sign == "tan":
        a *= math.pi / 180
        print(f"The Result is: {round(math.tan(a), 3)}")

    elif sign == "cos":
        a *= math.pi / 180
        print(f"The Result is: {round(math.cos(a), 3)}")

    elif sign == "cot":
        a *= math.pi / 180
        print(f"The Result is: {np.round(math.cos(a) / math.sin(a), 3)}")

    elif sign == "sqrt":
        print(f"The Result is: {np.round(math.sqrt(a), 3)}")

    elif sign == "factorial":
        a = int(a)
        print(f"The Result is: {math.factorial(a)}")

    else:
        print("Undefined Operation")
