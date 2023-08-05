#WAP to print only even number from 1 to 10
for num in range(0,11,2):
    print(num)

print("-----------------------------------")

#WAP to find the sum of elements of a given list of numbers
myList=[10,20,34,23,45,78,3,7,15]
totalSum=0
for element in myList:
    totalSum+=element
print(totalSum)

print("-----------------------------------")

#From a given list,, seperate odd and even and place them in different list
myList=[10,20,34,23,45,78,3,7,15]
listOdd=[]
listEven=[]
for num in myList:
    if num%2==0:
        listEven.append(num)
    else:
        listOdd.append(num)
print(f'The list for odd number is {listOdd}')
print(f'The list for even number is {listEven}')

print("-----------------------------------")

#WAP to seperate vowel and consonant from a given string and place in List
vowList=[]
conList=[]
spaceList=None
vowel=["a","e","i","o","u"]
val=0
userInput=input("Please enter a string: ")
for value in userInput:
    if value in vowel and value!=" ":
        vowList.append(value)
    elif value == " ":
        spaceList=value
    else:
        conList.append(value)
print(f'The vowel in string is {vowList}')
print(f'The consonant in string is {conList}')

print("-----------------------------------")

#WAP to separte names from list veginning with vowel and consonant
vowel=["a","e","i","o","u"]
vowelName=[]
consonantName=[]
nameList=["Ram","Shyam","Abhya","Sunny","Woof","Ian"]
for name in nameList:
    if name[0].lower() in vowel:
        vowelName.append(name)
    else:
        consonantName.append(name)
print(f'The name start from vowel is {vowelName}')
print(f'The name start from consonant is {consonantName}')

print("-----------------------------------")

print("-----------------------------------")

#WAP to separte names from list veginning with vowel and consonant// Using 2D element
vowel = ["a", "e", "i", "o", "u"]
vowelName = []
consonantName = []
nameList = ["Ram", "Shyam", "Abhya", "Sunny", "Woof", "Ian","Raja","Oala"]
counter = len(nameList)

for number in range(counter):
    if nameList[number][0].lower() in vowel:
        vowelName.append(nameList[number])
    else:
        consonantName.append(nameList[number])

print(f"The names starting with a vowel are: {vowelName}")
print(f"The names starting with a consonant are: {consonantName}")

print("-----------------------------------")

#WAP to seperate even and odd length names from a given list:
evenLengthName=[]
oddLengthName=[]
nameList = ["Ram", "Shyam", "Abhya", "Sunny", "Woof", "Ian","Raja","Oala"]
for name in nameList:
    if len(name)%2==0:
        evenLengthName.append(name)
    else:
        oddLengthName.append(name)
print(f"The names with even length are: {evenLengthName}")
print(f"The names with odd length are: {oddLengthName}")

##WAP to print a name in reverse
myStirng = "Prayush"
reverString=""
for char in myStirng:
    reverString=char+reverString
print(reverString)

#Reverse
myString= "Prayush"
myString2 = myString[::-1]
print(myString2)



