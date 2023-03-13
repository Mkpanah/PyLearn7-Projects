m = int(input("m = "))
n = int(input("n = "))

# Calculation of GCD
a = m
b = n
r = a % b
while r != 0:
    a = b
    b = r
    r = a % b

# Calculation of LCM
lcm = ((m / b) * n)
print(f"The LCM is {int(lcm)}.")


