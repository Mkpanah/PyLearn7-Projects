list_of_numbers = [74, 8, -95, 26, 81, 24, 12]
list_of_indexes = []
reversed_list_of_numbers = []

for i in range(len(list_of_numbers)):
    list_of_indexes.append(i)

for i in reversed(list_of_indexes):
    reversed_list_of_numbers.append(list_of_numbers[i])

print("The Original List is: ", list_of_numbers)
print("The Reversed List is: ", reversed_list_of_numbers)
