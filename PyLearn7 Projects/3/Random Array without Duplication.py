import random

n = int(input("The Length of Array : "))
value_range = range(0, 100)
my_list = []

for i in range(n):
    my_list.append(random.choice(value_range))

print(f"The Desired Random without Duplicates List between 0 and 100 is {set(my_list)}")