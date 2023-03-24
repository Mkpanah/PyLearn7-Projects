import math


def qubic_equation(a, b, c, d):
    while True:
        if (type(a) == str) or (type(b) == str) or (type(c) == str) or (type(d) == str):
            print("Enter Valid data type")
            break

        elif a == 0:
            print("Enter Qubic Equation's Requirements")
            break

        elif a != 1:
            b /= a
            c /= a
            d /= a
            a /= a

        epsilon = 10e-8
        p = c - ((b ** 2) / 3)
        q = ((2 * (b ** 3)) / 27) - (b * c / 3) + (d)
        delta = (q ** 2 / 4) + (p ** 3 / 27)

        if delta > epsilon:
            x = (((-q / 2) + math.sqrt(delta)) ** (1 / 3)) + (((-q / 2) - math.sqrt(delta)) ** (1 / 3)) - (b / 3)
            print(f"a = {a}, b = {b}, c = {c}, d = {d}")
            print(f"x = {x}")
            break

        elif -epsilon <= delta <= epsilon:
            x1 = -2 * ((q / 2) ** ( 1 / 3)) - b / 3
            x2 = ((q / 2) ** (1 / 3)) - b / 3
            print(f"x1 = {x1} and x2 = x3 = {x2}")
            break

        elif delta < 0:
            inv = math.asin((3 * math.sqrt(3) * q) / (2 * ((math.sqrt(-p)) ** 3)))
            x1 = (2 / math.sqrt(3)) * math.sqrt(-p) * math.sin((1 / 3) * inv) - (b / 3)
            x2 = (-2 / math.sqrt(3)) * math.sqrt(-p) * math.sin((1 / 3) * inv + (math.pi / 3)) - (b / 3)
            x3 = (2 / math.sqrt(3)) * math.sqrt(-p) * math.cos((1 / 3) * inv + (math.pi / 6)) - (b / 3)
            print(f"x1 = {x1} , x2 = {x2}, x3 = {x3}")
            break


qubic_equation(float(input("a = ")), float(input("b = ")), float(input("c = ")), float(input("d = ")))
