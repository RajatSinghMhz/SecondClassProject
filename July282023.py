import math


# #Function
# #Declaration of no return type and argument
# def giveMessage():
#     print("Hello World")
#
# #calling the function for execution// Calling done after declaration only in python// and can be used multiple times (Reuseable)
# giveMessage()
# giveMessage()
# print("___________________________________________________________________________________________________________________________")
#
# #WAP to ask user his name and  print it
# def askAndPrintName():
#     userInput=input("Enter your name: ")
#     print(userInput)
#
# askAndPrintName()
# print("___________________________________________________________________________________________________________________________")
#
# #Function with argument and parameters
# #WAP to sum of two number
# def sumOfTwo(x,y):
#     print(f'The sum of {x}+{y} is {x+y}')
# a=2
# b=4
# sumOfTwo(a,b)
# print("___________________________________________________________________________________________________________________________")
#
# # WAP to find the SI (Use function)
# def simpleInterest(p, t, r):
#     interest = (p * t * r / 100)
#     print(f'The simple interest of {p} principle, {r}% rate and {t} years is {interest}')
#
#
# simpleInterest(1000, 5, 10)
# print("___________________________________________________________________________________________________________________________")
#
#
# # WAP to area of circle
# def areaOfCircle(r):
#     area = 3.14 * (r) ** 2
#     print(area)
#
#
# areaOfCircle((5))
# print("___________________________________________________________________________________________________________________________")
#
#
# # WAP to find odd or even input
# def oddEvenCheck(num):
#     if num % 2 == 0:
#         print("Input is even")
#     elif num % 2 != 0:
#         print("Input is odd")
#     else:
#         print("Input is zero")
#
#
# userInputNum = int(input("Enter a number to check odd or even: "))
# oddEvenCheck(userInputNum)
# print("___________________________________________________________________________________________________________________________")

#WAP to make calculator:
def calculatorFunction(val,a,b):
    if val=="+":
        print(f'Sum is {a+b}')
    elif val=='-':
        print(f'Difference is {a-b}')
    elif val == '*':
        print(f'Product is {a*b}')
    elif val == '/':
        print(f'Division is {a/b}')
    else:
        print("Wrong input")
userInputOperator=input("Enter +,-,*,/ for the respective operations: ")
userInputnum1=input('Enter the first value: ')
userInputnum2=input("Enter the second value: ")

calculatorFunction(userInputOperator,int(userInputnum1),int(userInputnum2))


