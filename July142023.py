list=["Ram","Shyam","Hari","Gopal"]
#Access List
print(list)
print(list[0])
print(list[0][0])
print("_____________")

#Modify
list[0]="Ravan"
print(list)
print("_____________")

#Adding new element
list.append("Gita")
list.append("Rita")
print(list)
print("_____________")

list.insert(2,"Hello")
print(list)
print("_____________")
#Removing

list.remove("Hello")
list.pop(1)
print(list)
print("_____________")

#Sorting
list1=[1,5,2,3,9,7,8]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
print("_____________")

#Count and reverse only
list2=[2,4,9,2,8,5,2]
print(list2)
print(list2.count(2))
list2.reverse()
print(list2)
print("_____________")

#Concatenate and replacing multiple values
myList=[1,5,10,12,2,4,78,9]
myList[1:3]=[8]
print(myList)
myList1=[2,2]
myList=myList+myList1
print(myList)
print("_____________")

cars = ["Bmw", "Mazda", "honda", "chevrolet", "Bugati", "volkswagon", "tesla"]
x = len(cars)
print(x)
print("_____________")
print(f'{cars[0],cars[-1],cars[(x-1)//2]}')
print("_____________")
cars[cars.index("Bmw")] = "lamborghini"
print(cars)
print("_____________")
cars[1:3]=["Ford"]
print(cars)
print("_____________")
cars.append("Tata")
print(cars)
print("_____________")
cars.insert(2,"Mclaren")
print(cars)
print("_____________")
cars.remove("Bugati")
print(cars)
print("_____________")
print(cars.pop(3))
print(cars)
print("_____________")
bikes=["yamaha","Bajaj","Kawasaki","Ducati"]
cars.extend(bikes)
print(cars)
print("_____________")
cars.sort()
print(cars)
print("_____________")


