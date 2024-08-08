class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator
        for i in range(1, max(self.nominator, self.denominator)):
            if self.nominator % i == 0 and self.denominator % i == 0:
                self.gcd = i
        self.nominator = nominator // self.gcd
        self.denominator = denominator // self.gcd

    def represent(self):
        if self.denominator == 0:
            print("The denominator should not be zero")
        else:
            print(f"Standard : {self.nominator} / {self.denominator}")

    def decimal(self):
        if self.denominator == 0:
            print("The denominator should not be ZERO")
        else:
            print(f"Decimal : {self.nominator / self.denominator}")
            return self.nominator / self.denominator

    def simplification(self):
        if self.denominator == 0:
            print("The denominator should not be ZERO")
        else:
            for i in range(1, max(self.nominator, self.denominator)):
                if self.nominator % i == 0 and self.denominator % i == 0:
                    self.gcd = i
        print(f"The simplified form of the Fraction is :  {self.nominator / self.gcd} / {self.denominator / self.gcd}.")

    def quotient(self):
        if self.denominator == 0:
            print("The denominator should not be ZERO")
        else:
            print(f"Quotient : {self.nominator // self.denominator}")

    def reminder(self):
        if self.denominator == 0:
            print("The denominator should not be ZERO")
        else:
            print(f"Reminder : {self.nominator % self.denominator}")

    def add(self, other):
        if isinstance(other, Fraction):
            new_nominator = self.nominator * other.denominator + other.nominator * self.denominator
            new_denominator = self.denominator * other.denominator
            print(f"Addition : {new_nominator} / {new_denominator}")
        else:
            raise TypeError("Can only add Fraction to Fraction")

    def divide(self, other):
        if isinstance(other, Fraction):
            if other.nominator == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            new_nominator = self.nominator * other.denominator
            new_denominator = self.denominator * other.nominator
            print(f"Division : {new_nominator} / {new_denominator}")
        else:
            raise TypeError("Can only divide Fraction by Fraction")

    def subtract(self, other):
        if isinstance(other, Fraction):
            new_nominator = self.nominator * other.denominator - other.nominator * self.denominator
            new_denominator = self.denominator * other.denominator
            print(f"Subtraction : {new_nominator} / {new_denominator}")
        else:
            raise TypeError("Can only subtract Fraction from Fraction")

    def multiply(self, other):
        if isinstance(other, Fraction):
            new_nominator = self.nominator * other.nominator
            new_denominator = self.denominator * other.denominator
            print(f"Multiplication : {new_nominator} / {new_denominator}")
        else:
            raise TypeError("Can only multiply Fraction with Fraction")


first_fraction = Fraction(nominator=10, denominator=-6)
second_fraction = Fraction(nominator=-3, denominator=5)
first_fraction.represent()
first_fraction.decimal()
first_fraction.reminder()
first_fraction.quotient()
first_fraction.simplification()
first_fraction.add(second_fraction)
first_fraction.divide(second_fraction)
first_fraction.multiply(second_fraction)
first_fraction.subtract(second_fraction)
