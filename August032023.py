####################Write a program to double a number use return and argument
def doubleNumber(a):
    return a * 2


x = [2]
print("The double of number is: ", doubleNumber(x[0]))

z = map(lambda y: 2 * y, x)
print(list(z))
print("____________________________________________")


#######################Write a function to return true if even and false if odd
def oddEven(numCheck):
    if (numCheck % 2) == 0:
        return True
    else:
        return False

numCheck = 15
print(oddEven(numCheck))
print("____________________________________________")

################################### map SYntax: map(function-reference, iterable)// It often used to change lists
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
print("____________________________________________")

################################### lambda syntax is  variable=lambda expression:result// notes variable now acts as autonomous function::
newDoubler = lambda x: 2 * x
newTripler = lambda x: 3 * x
print(newDoubler(5))
print(newTripler(5))

newMyArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(newDoubler, newMyArray)))
print(list(map(newTripler, newMyArray)))
filteredArray=list(filter(lambda x: x % 2 == 0, myArray))
print(filteredArray)
print("____________________________________________")

######################### keyword argument Function
def myFunction(firstName,midName,lastName):
    print(firstName,midName,lastName)
myFunction(lastName="Maharjan",firstName="Rajat",midName="Singh")

print("____________________________________________")

########################## *args for dynamic function---returns tuple/// **kwargs return dictionary
def sumFunction(*num):
    sum=0
    for x in num:
        sum=sum+x
    print(sum)
sumFunction(1,2)
sumFunction(1,2,3)

def myFunctionSecond(**entryData):
    print(entryData)
myFunctionSecond(firstname="Rajat",lastname="Maharjan",age=27,married="False")

########################## Class and object
class Mammals:
    giveBirth=True
    scientificName="Mammalia"
    heartChamber=4
cow=Mammals()
print(cow.giveBirth)
print(cow.heartChamber)