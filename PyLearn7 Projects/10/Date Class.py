class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.validate()
        self.represent()

    def validate(self):
        if not (1 <= self.month <= 12):
            raise ValueError("Month must be between 1 and 12")
        if self.month in {1, 2, 3, 4, 5, 6}:
            if not (1 <= self.day <=31):
                raise ValueError("Invalid day for the given month and year.")
        if self.month in {7, 8, 9, 10, 11}:
            if not (1 <= self.day <= 30):
                raise ValueError("Invalid day for the given month and year.")
        if self.month == 12 and self.year % 4 == 3:
            if not (1 <= self.day <= 30):
                raise ValueError("Invalid day for the given month and year.")
        if self.month == 12 and self.year % 4 != 3:
            if not (1 <= self.day <= 29):
                raise ValueError("Invalid day for the given month and year.")

    def represent(self):
        my_dict = {
            1:"Farvardin",
            2:"Ordibehesht",
            3:"Khordad",
            4:"Tir",
            5:"Mordad",
            6:"Shahrivar",
            7:"Mehr",
            8:"Aban",
            9:"Azar",
            10:"Dey",
            11:"Bahman",
            12:"Esfand",
        }
        if self.day == 1:
            print(f"The desired Date is : {self.day}st Day of {my_dict[self.month]} Month of {self.year} year.")
        if self.day == 2:
            print(f"The desired Date is : {self.day}nd Day of {my_dict[self.month]} Month of {self.year} year.")
        if self.day == 3:
            print(f"The desired Date is : {self.day}rd Day of {my_dict[self.month]} Month of {self.year} year.")
        else:
            print(f"The desired Date is : {self.day}th Day of {my_dict[self.month]} Month of {self.year} year.")


date1 = Date(year=1397, month=1, day=13)

