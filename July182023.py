#WAP to print sum of odd number and even numbers 1 to 20 and which shows is greater.
num=1
odd=0
even=0
great=[]
while num<=20:
    if num%2!=0:
        odd=odd+num
    else:
        even=even+num
    great.append(num)
    num+=1
if odd>even:
    print("Sum of odd is greater")
elif odd<even:
    print("Sum of even is greater")
else:
    print("Both sum is equal")
great.sort()
print(f'Sum of odd is {odd}')
print(f'Sum of even is {even}')
print(great[-1])
print(great)

#Build a car game (break)//
count=0
while count!=3:
    playerEntry=input("Start/ Stop/ Quit")

    if playerEntry.upper()=="START":
        print("Car has started")
    elif playerEntry.upper()=="STOP":
        print("Car has stopped")
    elif playerEntry.upper()=="QUIT":
        print("Quitting the game")
        break
    else:
        print("Unknown command, try again")

#WAP to demonstrate your phones pin checker
pin="1989"
check=4
while check!=0:
    pinCompare=input("Enter your pin")
    if pinCompare=="1989":
        print("Mobile Unlocked")
        break
    else:
        print(f'You have {check-1} attempts left.')
        check-=1

#Example of break and continue
count=0
while count<=10:
    count=count+1
    if count==2:
        print("2 is reached")
        continue
    print(count)

######FOr Loop########
myList=[12,234,5,67,8,90,12]
for i in myList:
    print (i)

#WAP to create a list of 10 elements and print each element.
newList=[1,2,3,4,5,6,7,8,9,10]
user=[]
for value in newList:
    userInput=input("Values")
    user.append(userInput)
print(user)

#WAP to iterate over a list and print only even number of that list
numList=[1,2,3,4,5,6,7,8,9,10]
for even in numList:
    if even%2==0:
        print (even)
    else:
        continue

#WAP to iterate over a list and print only odd
numList=[1,2,3,4,5,6,7,8,9,10]
for even in numList:
    if even%2!=0:
        print (even)
    else:
        continue

#WAP to iterate a list and count number of odd and even
numListnew=[1,2,3,4,5,6,7,8,9,10,13,156,489,159,1]
countEven=0
countOdd=0
for numin in numListnew:
    if numin%2==0:
        countEven+=1
    else:
        countOdd+=1
print(f'The number of odd in list is {countOdd}')
print(f'The number of even in list is {countEven}')

#WAP to create a list of student names and count number of vowel
list="python is a programming language"
vowelList=["a","e","i","o","u"]
counter=0
for vowel in list:
    if vowel in vowelList:
        counter=counter+1
print(f'The number of vowels in \"{list}\" is {counter}')

