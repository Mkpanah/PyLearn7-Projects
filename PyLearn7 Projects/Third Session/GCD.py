m = int(input("m = "))
n = int(input("n = "))

# Euclidean Algorithm for GCD
r = m % n
while r != 0:
    m = n
    n = r
    r = m % n

print(f"The GCD is {n}.")