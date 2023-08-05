
#Voting rights
ageString=input("Enter your age in number")
ageValue=int(ageString)
if ageValue>18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

### Check if user entered number is odd or even

userEnteredNumber = int(input('Enter the number'))
if (userEnteredNumber % 2) == 0 :
    print ('It is even')
else:
    print("It is odd")

#Compare two numbers
numCompare1 = int(input("Enter number1"))
numCompare2 = int(input("Enter number2"))
if numCompare1 > numCompare2 :
    print(f'The greater number out of {numCompare1} and {numCompare2} is {numCompare1}')
elif numCompare1 == numCompare2 :
    print("Both are equal")
else:
    print(f'The greater number out of {numCompare1} and {numCompare2} is {numCompare2}')

#Access to class

userCard=input(" Have you brought your card Y or N ")
if userCard.upper() == "Y":
    print("Welcome to the class")
elif userCard.upper() == "N":
    print("Print bring your card")
else :
    print("Invalid Input")

#Operation of choice
userNum1 = int(input("Enter first number"))
userNum2 = int(input("Enter second number"))
userOperator = input("Enter one operator (+,-,/,*)")
if userOperator == "+":
    print(f' The sum is {userNum2+userNum1}')
elif userOperator == "-":
    print(f' The difference is {userNum1 - userNum2}')
elif userOperator == "*":
    print(f' The product is {userNum2 * userNum1}')
else:
    print(f' The division is {userNum1 / userNum2}')

#Make a small dictionary
dictionary_list="Hello this is a random text containing some random data of python"
string_search=input(" Enter the string to search")
result=dictionary_list.find(string_search)
if result!= -1:
    print(f'String found in position {result}')
else:
    print("Not found")

