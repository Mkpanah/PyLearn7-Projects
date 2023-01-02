# Insert first side's value of Triangle
first_side = float(input("Enter 1st Side's Value = "))
# Insert second side's value of Triangle
second_side = float(input("Enter 2nd Side's Value = "))
# Insert third side's value of Triangle
third_side = float(input("Enter 3rd Side's Value = "))

# Different set of Conditions
if first_side > (second_side + third_side):
    print("Impossible to draw this Triangle.")
elif second_side > (first_side + third_side):
    print("Impossible to draw this Triangle.")
elif third_side > (second_side + first_side):
    print("Impossible to draw this Triangle.")
else:
    print("Possible to draw this Triangle.")
