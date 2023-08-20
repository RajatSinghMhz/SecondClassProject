# 1) WAP to create a class representing rectangle.Include methods to calculate its area and perimeter.
class Rectangle:
    def __init__(self,length,breadth):
        self.length =length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimetrer(self):
        return 2 * (self.length + self.breadth)

rectangle1 = Rectangle(5,5)
print(f'The area is {rectangle1.area()}')
print(f'The perimeter is {rectangle1.perimetrer()}')

# 2) WAP which includes attributes like name, country and date of birth.Write a method to determine the person's age.
from datetime import date
class Person:
    def __init__(self,name,country,dob):
        self.name =name
        self.country = country
        self.dob = dob

    def age(self):

        #using datetime package to get todays date
        today = date.today()

        #splitting the string date by -
        dobs =self.dob.split("-")
        print(type(dobs))
        print(dobs)

        #Converting the date to date time object
        dobConverted = date(int(dobs[0]), int(dobs[1]), int(dobs[2]))
        print(dobConverted)

        #getting the difference in date
        ageinDays = today - dobConverted

        #changing days to years
        age = round(ageinDays.days/365)
        return age

person1 = Person('prayush','ktm','1996-01-07')
print(f'The age is {person1.age()}')

# 3) WAP to create a class that represents a shape.Write methods calculate its area and perimeter. Also
# have subclasses for different shapes like circle, triangle, and square.

class Shape:
    def __init__(self,length):
        self.length =length


class Circle(Shape):
    pie = 3.1415

    def __init__(self,len):
        super().__init__(length=len)

    def area(self):
        return self.pie * self.length

c1 = Circle(5)
print(f'The area of circle is {c1.area()}')

class Triangle(Shape):

    def __init__(self,len,b,h):
        super().__init__(length=len)
        self.b = b
        self.h = h

    def area(self):
        return (1/2) * (self.b * self.h)

    def perimeter(self):
        return self.length + self.b + self.h

t1 = Triangle(5,10,15)
print(f'The area of triangle is {t1.area()}')


# 4)You have two files Keys and values. Create a dictionary from that file and display.
keyFile = open('keys','r')
valueFile = open('values','r')
allKeys = []
allValues = []
for keys in keyFile.readlines():
    allKeys.append(keys[:-1])

for values in valueFile.readlines():
    allValues.append(values[:-1])

####Zip takes two array and changes to dictionary
dict = dict(zip(allKeys,allValues))
print(f'Dictionary from zip {dict}')

#alternative
myDict = {}
for counter in range(len(allKeys)):
    myDict[allKeys[counter]] = allValues[counter]

print(f'Dictionary from alternate {myDict}')


# 5)Write a program to create a searching algorithm ( Assume that the text is store in a file )

searchFile = open('SearchFIle.txt','r')

fileContents = searchFile.read()
userInput = input('Enter the value to search :')

if fileContents.find(userInput) !=-1:
    print('Present')

else:
    print('Not Present')

