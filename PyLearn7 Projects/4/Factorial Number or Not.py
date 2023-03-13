n = int(input("Number = "))

for i in range(1, n+1):
    if n % i == 0:
        n /= i
    else:
        break

if n == 1:
    print("Yeah")
else:
    print("Nope")
