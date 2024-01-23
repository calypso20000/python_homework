# Create a Python class representing a basic calculator with methods for addition, subtraction, multiplication, and division.

class BasicCalculator:
    def __init__(self, number1=0, number2=0):
        self.number1=number1
        self.number2=number2

    def addition(self):
        return self.number1+self.number2
    def subtraction(self):
        return self.number1-self.number2
    def multiplication(self):
        return self.number1*self.number2
    def division(self):
            return self.number1/self.number2
        

result=BasicCalculator()
result.number1=8 
result.number2=2
print(result.addition())
print(result.subtraction())
print(result.multiplication())
print(result.division())