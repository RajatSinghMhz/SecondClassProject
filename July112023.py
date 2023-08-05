import  random

#Check positive, negative, zero.

numCheck=int(input("Enter any integer number "))
if numCheck>0:
    print(f'The given number {numCheck} is Positive. ')
elif numCheck<0:
    print(f'The given number {numCheck} is Negative. ')
else:
    print(f'The given number is Zero. ')
#WAP to generate random number
randomNumber=random.randint(0,100)
print(f'The random number is {randomNumber}')

print("------------------------------------------")

#WAP to simulate guessing game
userGuess=int(input("Enter the guessing number"))
randomValue=random.randint(0,10)
if userGuess>10:
    print("You have exceeded the limit")
elif userGuess<0:
    print("You are below the limit.")
elif userGuess==randomValue:
    print(f'You have guessed the random number {randomValue} correctly')
else:
    print("Better try luck next time")

print("------------------------------------------")

#WAP to create user id and password validator ask input from user
username="ram"
password="ram123"
usernameinput=input("Enter your username")
passwordinput=input("Enter your password")

if usernameinput==username and passwordinput==password:
    print("Welcome, you are a valid member")
elif usernameinput==username and passwordinput!=password:
    print("Please try again")

print("------------------------------------------")

#WAP to check if the user allowed to vote or not ask if the user is student(s) or Teacher(t)
voter1=input("Are you a student Y or N: ")
voter2=input("Are you a teacher Y or N: ").upper()
if voter1.upper()=="Y" or voter2=="Y":
    print("You are allowed to vote. ")
else:
    print("You're not allowed to vote. ")

print("------------------------------------------")

#WAP to create lucky draw with multiple prizes giving weight
# prize=["Coke","Fanta","Watch","Laptop","Mobile"]
# value=random.randint(0,4)
# print(f'Congratulations you have won a {prize[value]}')
lottery=random.randint(0,100)
if lottery==5:
    print("Congrats you won the bumper prize,IPHONE")
elif (lottery>=0 and lottery<40) or (lottery>60 and lottery<80):
    print("Sorry better look next time")
else:
    print("You have won a pen")

print("------------------------------------------")

#WAP to compare greater number between three numbers.
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))
greatest=None
lowest=None
if num1>num2 and num1>num3:
    greatest=num1
    if num2>num3:
        lowest=num3
    else:
         lowest=num2
elif num2>num3 and num2>num1:
    greatest=num2
    if num1>num3:
        lowest=num3
    else:
         lowest=num1
else:
    greatest=num3
    if num1>num2:
        lowest=num2
    else:
          lowest=num1
print(f' The greatest and lowest of {num1},{num2},{num3} is {greatest} and {lowest}')





