# WAP to write name of 5 people in file asking input from the user

## Assuming that the file contents all the marks of grade 11 student, calculate the percentage,grade,highest,lowest marks
# and store in a file

# namePath=r'FileDirectory/August062023_Homework'
# nameFile=open(namePath,'w')
# username=[]
# for nameCount in range(0,5):
#     name=input(f'Enter the name of person no {nameCount+1}: ')
#     username.append(name)
#     nameCall=nameFile.write(username[nameCount])
#     nameCall=nameFile.write("\n")
# nameFile.close()
def total(*a):
    return sum(a)
def percent(b,c):
    return b * 100 /c

gradePath = r'FileDirectory/August062023_Extraction'
gradeFile = open(gradePath, 'r')
gradeVar = gradeFile.readlines()
count = 0
marks = []
for i in range(0, 12):
    marks.append(int(gradeVar[i].strip()))
marks.sort(reverse=True)

totalMark=total(*marks)
percentage=percent(totalMark,len(marks)*100)

savePath = r'FileDirectory/August062023_ExtractionSave'
saveFile = open(savePath, 'w')
newList=[
    "Total Marks","=",str(totalMark),"\n",
    "Total Percentage","=",str(percentage),"\n",
    "Highest Marks","=",str(marks[0]),"\n",
    "Lowest Marks","=",str(marks[-1]),"\n"
    ]
saveFile.writelines(newList)
saveFile.close()

# WAP to create a simple billing system
# 1) Display the menu to user from file
# 2) Create a dictionary with same menu items key as item and price as value
# 3) In loop until user enters quit ask user item and quantity to order and store
# 4) display a bill with 13% vat and store in file

menuPath=r'FileDirectory/August062023_Menu'
menuFile=open(menuPath,'r')
menu=menuFile.read()
print(f'Here is this menu: \n{menu}')

# def display_menu(menu):
#     print("Menu:")
#     for item, price in menu.items():
#         print(f"{item}: ${price:.2f}")
#
# def calculate_total(order, menu):
#     total = 0
#     for item, quantity in order.items():
#         total += menu[item] * quantity
#     return total
#
# def main():
#     # Load menu from file into a dictionary
#     menu = {}
#     with open("FileDirectory/August062023_Menu", "r") as menu_file:
#         for line in menu_file:
#             item, price = line.strip().split(",")
#             menu[item] = float(price)
#
#     order = {}
#     while True:
#         display_menu(menu)
#         item = input("Enter the item you want to order (or 'quit' to exit): ")
#         if item.lower() == 'quit':
#             break
#
#         if item in menu:
#             quantity = int(input(f"How many {item}s do you want to order? "))
#             if item in order:
#                 order[item] += quantity
#             else:
#                 order[item] = quantity
#         else:
#             print("Invalid item. Please choose from the menu.")
#
#     total_amount = calculate_total(order, menu)
#     vat = 0.13 * total_amount
#     total_with_vat = total_amount + vat
#
#     print("\n\n----- Bill -----\n")
#     for item, quantity in order.items():
#         print(f"{item} x {quantity}: ${menu[item] * quantity:.2f}")
#     print(f"\nTotal: ${total_amount:.2f}")
#     print(f"VAT (13%): ${vat:.2f}")
#     print(f"Total (including VAT): ${total_with_vat:.2f}")
#
#     with open("bill.txt", "w") as bill_file:
#         bill_file.write("----- Bill -----\n\n")
#         for item, quantity in order.items():
#             bill_file.write(f"{item} x {quantity}: ${menu[item] * quantity:.2f}\n")
#         bill_file.write("\n")
#         bill_file.write(f"Total: ${total_amount:.2f}\n")
#         bill_file.write(f"VAT (13%): ${vat:.2f}\n")
#         bill_file.write(f"Total (including VAT): ${total_with_vat:.2f}\n")
#
# if __name__ == "__main__":
#     main()

