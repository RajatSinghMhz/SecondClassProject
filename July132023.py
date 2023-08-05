
# WAP to calculate the water bill according to the following criteria
#
# Units				Price
# First 100 			No charge
# Next 100			Rs 5 per unit
# After 200			Rs 10 per unit

waterUnit=int(input("Enter the water bill unit: "))
if waterUnit<=100:
    print("No Charge")
if waterUnit>100 and waterUnit<=200:
    print(f'Your total charge is Rs.{(waterUnit-100)*5}')
if waterUnit>200:
    print(f'Your total charge is Rs.{0+100*5+(waterUnit-200)*10}')

# Write a program to accept percentage from the user and display the grade according to the following criteria:
#
#          Marks                                Grade
#          > 90                                 A
#          > 80 and <= 90                       B
#          >= 60 and <= 80                      C
#          below 60                             D
marksUser=int(input("Enter your percentage: "))
if(marksUser>90):
    print("Grade A")
elif(marksUser>80 and marksUser<=90):
    print("Grade B")
elif(marksUser>=60 and marksUser<=80):
    print("Grade C")
else:
    print("Grade D")

#Create 18 people list and extract first, second, last middle element.
list1=["A","B","C","D","E","F",'G',"H","I","J","K","L","M","N","O","P","Q","R"]
print(list1[0],list1[1],list1[-1],list1[((len(list1)-1)//2)])

#WAP to find the first letter of first element of string array.
list2=["Ram","Shyam","Hari","Gopal"]
print(list2[0][0])

#WAP to check if first letter of element of string list is vowel or not.
listCheck=["a","e","i","o","u"]
list3=["Ram","Shyam","Hari","Gopal","Iush"]
if (list3[4][0].lower()==listCheck[0] or list3[4][0].lower()==listCheck[1] or list3[4][0].lower()==listCheck[2] or list3[4][0].lower()==listCheck[3] or list3[4][0].lower()==listCheck[4]):
    #if list3[4][0].lower() in listCheck:
    print("Vowel")
else:
    print("Consonant")

