class ComplexNumbers:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        self.new_real = None
        self.new_imaginary = None

    def addition(self, real=0, imaginary=0):
        self.real += real
        self.imaginary += imaginary
        return self.real, self.imaginary

    def subtraction(self, real=0, imaginary=0):
        self.real -= real
        self.imaginary -= imaginary
        return self.real, self.imaginary

    def multiplication(self, real=0, imaginary=0):
        self.new_real = (self.real * real) - (self.imaginary * imaginary)
        self.new_imaginary = (self.real * imaginary) + (self.imaginary * real)
        return self.new_real, self.new_imaginary


first_complex_number = ComplexNumbers(real=+2, imaginary=-1)
added_real, added_imaginary = first_complex_number.addition(real=-1, imaginary=3)
subtracted_real, subtracted_imaginary = first_complex_number.subtraction(real=-2, imaginary=1)
multiplication_real, multiplication_imaginary = first_complex_number.multiplication(real=-1, imaginary=2)
print(f"Addition result : {added_real} + {added_imaginary}i")
print(f"Subtraction result : {subtracted_real} + {subtracted_imaginary}i")
print(f"Multiplication result : {multiplication_real} + {multiplication_imaginary}i")
