list_of_numbers = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : ", list_of_numbers)


list_without_duplicates = []
[list_without_duplicates.append(number) for number in list_of_numbers if number not in list_without_duplicates]

print("The list after removing duplicates : ", list_without_duplicates)
