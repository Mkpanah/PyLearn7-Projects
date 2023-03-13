# Insert Name
name = input("Please insert your Name: ")
# Insert Family Name
family = input("Please insert your Family name: ")
# Insert First Lesson's Grade in 0 to 20 Scale
first_grade = float(input("1st Lesson's Grade = "))
# Insert Second Lesson's Grade in 0 to 20 Scale
second_grade = float(input("2nd Lesson's Grade = "))
# Insert Third Lesson's Grade in 0 to 20 Scale
third_grade = float(input("3rd Lesson's Grade = "))

# Calculation of Average
average = (first_grade + second_grade + third_grade) / 3

# Handling Improper Values for Grades
if first_grade > 20 or second_grade > 20 or third_grade > 20:
    print("Please insert Proper Grade in 0 to 20 Scale.")
else:
    if average >= 17:
        print(f"{name} {family},You're Average is {round(average, 3)} and You are Great")
    elif 12 <= average < 17:
        print(f"{name} {family},You're Average is {round(average, 3)} and You are Normal")
    else:
        print(f"{name} {family},You're Average is {round(average, 3)} and You Failed")
