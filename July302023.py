# #WAP using function to check if a given value is array?
# arrayBlock=[1,2,3,"Rajat","Ashish","Prayush"]
# def checkString(valueInput):
#     if valueInput in arrayBlock:
#         print("It is in our database")
#     else:
#         print("Sorry it is not in out database ")
#
# valueInput=input("Enter any number or string to check in database ")
#
# checkString(valueInput)

# #WAP to multiply each member of array of value by a given number, do not take input:
# array=[2,4,6,8,10,12]
# def permutationCombo():
#     multiplyAray = []
#     for x in array:
#         for y in array:
#             multiplyAray.append(x*y)
#     return multiplyAray
#
# print(permutationCombo())

# #map and lamba try
# array=[2,4,6,8,10,12]
# paraFunc=map(lambda x: array*x,array)
# print(list(paraFunc))
#
# #Wap to calculate SI and final result of one execution in NPR and next in INR
# def interestS (p,t,r):
#     return (p*t*r)/100
# def inrS(x):
#     return x/1.6
#
# userInputPrinciple=int(input("Enter principle: "))
# userInputTime=int(input("Enter time: "))
# userInputRate=int(input("Enter rate: "))
# y=interestS(userInputPrinciple,userInputTime,userInputRate)
# print("In NPR: ",y)
# print("In INR: ",inrS(y))

# #WAP to get only even number from an array usig function and dispaly it in new array
# array=[2,4,6,8,10,12,1,3,5,7,9,34,16,13]
#
# def displayFunc(a):
#     print(a)
# def evenCheck():
#     for x in array:
#         if x%2==0:
#             displayFunc(x)
# y=evenCheck()

#MAP-----------map (function, iterable)---iterable size=result size-------Gives exact what is returned
#Filter--------filter(function, iterable)--iterable size> result size-----Gives only real values

myArray=[2,4,6,8,10,12,1,3,5,7,9,34,16,13]
newArray=map(lambda x:x*2,myArray)
newArray2=filter(lambda x:x%2==0,myArray)
print(list(newArray))
print(list(newArray2))

#Filter removes returned None values, while map or calling function won't do it.


