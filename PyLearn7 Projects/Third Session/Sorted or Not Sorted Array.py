n = int(input("The Length of Array : "))

my_array = []
for i in range(n):
    my_array.append(float(input("Number: ")))

print(f"Entered Array is : {my_array}")

is_sorted = [a <= b for a, b in zip(my_array, my_array[1:])]

if False in is_sorted:
    print("The Array is Not Sorted.")
if False not in is_sorted:
    print("The Array is Sorted.")

# print(list(zip(test_list, test_list[1:])))