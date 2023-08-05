# #List
# Ordered
# Mutable
# Allow Duplication
# []

# #String
# Ordered
# Not Mutable
# Allow Duplication
# ""

# #Dictionary
# Mutable
# No particular order of element
# No Duplication
# Key:Value pair
# {}
#
# Syntax:
# variable={
#
# }

myCart=[100,120,130,50,60]
myCartItem=["Tomato","Potato","Apple","Banana","Grapes"]
myDictionaryCart={
    "Tomato":100,
    "Potato":120,
    "Apple":130,
    "Banana":50,
    "Grapes":60
}
print(myCart)
print("______________________")
print(myCartItem)
print("______________________")
print(myDictionaryCart)
print("______________________")
print("______________________")

#Access (2 method)
price=myDictionaryCart["Tomato"]
print(price)
price2=myDictionaryCart.get("Banana")
print(price2)
print("______________________")

#Update
myDictionaryCart["Tomato"]=120
print(myDictionaryCart)
print("______________________")

#Insert
myDictionaryCart["New Fruit"]=500
print(myDictionaryCart)

#Delete
myDictionaryCart.pop("grapes".capitalize())
print(myDictionaryCart)
print("______________________")
print("______________________")

#loop input
for x in range(1,4):
    userFood=input("Enter the food: ")
    userPrice = input("Enter the price: ")
    myDictionaryCart[userFood]=userPrice
print(myDictionaryCart)

