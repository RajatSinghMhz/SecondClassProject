# # WAP to write name of 5 people in file asking input from the user
#
# filePath = r'FileDirectory/August062023_Homework'
# file = open(filePath,'w')
# for x in range(5):
#     name = input("Enter the name :")
#     file.write(name)
#     file.write('\n')
# file.close()
#

# Assuming that the file contents all the marks of grade 11 students, calculate the percentage,grade,highest,lowest marks and store in a file

import math

filepath = r'FileDirectory/August062023_Extraction'
filepathResult = r'FileDirectory/August062023_ExtractionSave'
file = open(filepath, 'r')
fileWrite = open(filepathResult, 'w')
marks = file.readlines()
totalObtained = 0
newMarks = 0
newList = []
for mark in marks:
    newMarks = int(mark.strip())
    totalObtained = totalObtained + newMarks
    newList.append(newMarks)
newList.sort()
highestMarks = newList[-1]
lowestMarks = newList[0]
totalMarks = len(newList) * 100
percentage = (totalObtained / totalMarks) * 100

fileWrite.write('DAV HIGHER SECONDARY SCHOOL \n')
fileWrite.write('FIRST TERM RESULT\n')
fileWrite.write(f'LOWEST MARKS {lowestMarks} \n')
fileWrite.write(f'HIGHEST MARKS {highestMarks} \n')
fileWrite.write(f'PERCENTAGE {round(percentage)} \n')

# WAP to create a simple billing system
# 1) Display the menu to user from file
# 2) Create a dictionary with same menu items key as item and price as value
# 3) In loop until user enters quit ask user item and quantity to order and store
# 4) display a bill with 13% vat and store in file


menuList = {
    'momo':250,
    'chowmein':200,
    'coke':50,
    'water':20
}
filepath=r'FileDirectory/August062023_Menu'
file = open(filepath,'w')
orders = {}

menuItems = list(menuList.keys())
quit = False

while not quit:

    userValue = input("Enter the item name ")
    if userValue == 'quit':
        break
    if userValue.lower() not in menuItems:
        print('The Item You entered is not present, Please check menu correctly')
        continue
    userOrder = int(input("Enter the quantity "))
    orders[userValue] = userOrder * menuList[userValue]

file.write(f'Chubbyz Chicken\n')
file.write(f'Item\t\t\t Amount\n')
totalPrice = 0
for item in orders.items():
    totalPrice = totalPrice + item[1]
    file.write(f'{item[0]}\t\t\t {item[1]}\n')

vat = totalPrice * 0.13
grandTotal = totalPrice + vat
file.write(f'=========================')
file.write(f'Total\t\t\t {totalPrice}\n')
file.write(f'Vat\t\t\t   {vat}\n')
file.write(f'=========================')
file.write(f'Grand Total\t\t {grandTotal}')



