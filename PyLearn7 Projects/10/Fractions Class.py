class Fraction:
    def __init__(self, nominator, denominator, sign):
        self.nominator = nominator
        self.denominator = denominator
        self.sign = sign

    def decimal(self):
        if self.denominator == 0:
            return "The denominator should not be ZERO"
        elif self.sign == "+":
            return f"Decimal : {self.nominator / self.denominator}"
        elif self.sign == "-":
            return f"Decimal : {-1 * self.nominator / self.denominator}"

    def quotient(self):
        if self.denominator == 0:
            return "The denominator should not be ZERO"
        elif self.sign == "+":
            return f"Quotient : {self.nominator // self.denominator}"
        elif self.sign == "-":
            return f"Quotient : {-1 * (self.nominator // self.denominator)}"

    def reminder(self):
        if self.denominator == 0:
            return "The denominator should not be ZERO"
        elif self.sign == "+":
            return f"Reminder : {self.nominator % self.denominator}"
        elif self.sign == "-":
            return f"Reminder : {-1 * (self.nominator % self.denominator)}"


first_fraction = Fraction(12, 7, "+")
print(first_fraction.decimal())
print(first_fraction.reminder())
print(first_fraction.quotient())
