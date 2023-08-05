class Cars:
    wheel = 4
    seatbelt = True
    color = ""
    company = ""

    print("__________________________________________________")

    ###########Constructor
    def __init__(self, a, b):
        self.color = a
        self.company = b


jeep = Cars("Green", "JeepUS")
print(jeep.color)
print(jeep.company)

print("__________________________________________________")

wagnonr = Cars("Blue", "Marcedes")
print(wagnonr.color)
print(wagnonr.wheel)


# Create a class student include school and dress as common parameter, name, age and class from constructor
class Student:
    school = "DAV"
    dress = "Maroon"
    name = ""
    age = ""
    classes = ""

    #####Constructor// Runs to assign data to variables
    def __init__(self, name, age, classes):
        self.name = name
        self.age = age
        self.classes = classes

    ###Methods// can be used like function call
    def greeting(self):
        return print(f'Hello I am {self.name} and {self.age} years old.')

    # Return// Returns particular structure or format or use built in function instead of metos
    def __str__(self):
        return f'{self.name} is of age {self.age} and studies in class {self.classes}'


ram = Student("Ram", "27", "12")
rajat = Student("Rajat", "27", "17")
kushal = Student("Kushal", "19", "12")

print(ram)
print(rajat)
print(kushal)
ram.greeting()


############Create a class calculator that takes two nubers from constructor and has 4 arithmetic methods that returns prints result
class Calculator:
    number1 = ""
    number2 = ""
    operator = ""

    def __init__(self, number1, number2, operator):
        self.number1 = number1
        self.number2 = number2
        self.operator = operator

    def add(self):
        return self.number1 + self.number2

    def __str__(self):
        if self.operator == "+":
            return f"{int(self.number1) + int(self.number2)}"
        elif self.operator == "-":
            return f"{int(self.number1) - int(self.number2)}"
        elif self.operator == "*":
            return f"{int(self.number1) * int(self.number2)}"
        elif self.operator == "/":
            return f"{int(self.number1) / int(self.number2)}"
        else:
            return f"Invalid"


addition = Calculator(2, 3, "+")
subtraction = Calculator(2, 3, "-")
multiplication = Calculator(2, 3, "*")
division = Calculator(2, 3, "/")
print(f"The generated add by metos is {addition.add()}")
print(addition)
print(subtraction)
print(multiplication)
print(division)

######################## Inheritance
class Father:
    caste="Shrestha"
    def __init__(self,name):
        self.name=name

    def fatherfunction(self):
        print(f"Hello, I am the father of {self.name}")
class Children(Father):
    gender=""
    name=""
    def __init__(self,gender,name):
        self.gender=gender
        super().__init__(name)

    def childFunction(self):
        print("Hello I am child")
c1=Children("Boy","Ram")
print (c1.fatherfunction())