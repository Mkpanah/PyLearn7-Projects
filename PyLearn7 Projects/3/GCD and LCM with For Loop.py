gcd = 0
lcm = 0
a = int(input("First Number: "))
b = int(input("Second Number: "))

for i in range(1, max(a, b)):
    if a % i == 0 and b % i == 0:
        gcd = i

for i in reversed(range(1, (a * b) + 1)):
    if i % a == 0 and i % b == 0:
        lcm = i


print(f"LCM is {lcm}.")
print(f"GCD is {gcd}")