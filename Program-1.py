# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#     Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#     Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string



# solution 1:

class calculator:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.result = 0
        self.operator = ''

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def set_operator(self, operator):
        self.operator = operator

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_result(self):
        return self.result

    def get_operator(self):
        return self.operator

    def add(self,a, b):
        return a + b    # Addition

    def subtract(self,a, b):
        return a - b    # Subtraction

    def multiply(self,a, b):
        return a * b    # Multiplication

    def divide(self,a, b):
        return a / b    # Division

    def calculate(self):
        if self.operator == '+':
            self.result = self.add(self.a, self.b)
        elif self.operator == '-':
            self.result = self.subtract(self.a, self.b)
        elif self.operator == '*':
            self.result = self.multiply(self.a, self.b)
        elif self.operator == '/':
            self.result = self.divide(self.a, self.b)
        else:
            print("Invalid operator")


calculator = calculator()
calculator.set_a(float(input("Enter first number: ")))
calculator.set_b(float(input("Enter second number: ")))
calculator.set_operator(input("Enter operator: "))
calculator.calculate()
print("Result: ", calculator.get_result())
