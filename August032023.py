# Write a program to double a number use return and argument
import random


def doublenumber(a):
    return a * 2


x = [2]
print("The double of number is: ", doublenumber(x))
print("The double of number is: ", doublenumber(x[0]))
# If you multiply list, it will replicate itself that times,, so if you want to multiple inside value, use indexing.
# Now lets use lambda function to replace function(doubleNumber) and use map to call function:: to do the same:

z = map(lambda y: 2 * y, x)
print(list(z))
print("______________________________________________________________________________")


# Write a function to return true if even and false if odd
def oddEven(numCheck):
    if (numCheck % 2) == 0:
        return True
    else:
        return False


numCheck = random.randint(0, 100)
print(numCheck)
print(oddEven(numCheck))
print("______________________________________________________________________________")

# map Syntax: map(function-reference, iterable)// It often used to change lists
# Write a program using map and filter to double and triple:
myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def doubler(x):
    return x * 2


def triple(x):
    return x * 3


newArrayDouble = map(doubler, myArray)
print(list(newArrayDouble))

newArrayTriple = map(triple, myArray)
print(list(newArrayTriple))

myFilteredArray = filter(oddEven, myArray)
print(list(myFilteredArray))
# This will print even list only,, so simply imagine filter same as map but gives value based on Boolean
print("______________________________________________________________________________")

# lambda syntax is  variable=lambda expression:result//
newDoubler = lambda x: 2 * x
newTripler = lambda x: 3 * x
# Notes variable now acts as autonomous function // simply imagine this as defining a function in one line
print(newDoubler(5))
print(newTripler(5))

print("______________________________________________________________________________")

newMyArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(newDoubler, newMyArray)))
print(list(map(newTripler, newMyArray)))
# map takes newDoubler as function and iteration set as newMyArray, then stores it in memory
# Then to print that data in memory we need to typecast it using "list" to change it into readable format.
filteredArray = list(filter(lambda x: x % 2 == 0, myArray))
print(filteredArray)
print("______________________________________________________________________________")


# keyword argument Function // We use this to assign data in function in random order
def myFunction(firstName, midName, lastName):
    print(firstName, midName, lastName)


myFunction(lastName="Maharjan", firstName="Rajat", midName="Singh")

print("______________________________________________________________________________")


# *args for dynamic function---returns tuple/// **kwargs return dictionary
def sumFunction(*num):
    sum = 0
    for x in num:
        sum = sum + x
    print(sum)


sumFunction(1, 2)
sumFunction(1, 2, 3)

print("______________________________________________________________________________")

# Here we used dynamic way of assigning value to argument, since we don't know how many inputs we have each time.
# In first iteration, there were two input, in second there were three inputs.

def myFunctionSecond(**entryData):
    print(entryData)
    print(entryData.keys())
    print(entryData.values())


myFunctionSecond(firstname="Rajat", lastname="Maharjan", age=27, married="False")


# Here another dynamic method is used "kwargs" denoted by **autonomous function
# Since this method return dictionary, input should be in dictionary format of key and value.

print("______________________________________________________________________________")

# Class and object
class Mammals:
    giveBirth = True
    scientificName = "Mammalia"
    heartChamber = 4

cow = Mammals()
print(cow.giveBirth)
print(cow.heartChamber)
