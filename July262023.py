##CREATE A PROGRAM TO UNIQUIFY THE LIST
#EG : [10,20,30,10,50] should return [10,20,30,50]
myList=[10,20,30,10,50]
uniqueList=[]
for x in myList:
    if x not in uniqueList:
        uniqueList.append(x)
print(uniqueList)
print("_______________")

#WAP to do simple database check:
teacherArray=[
    {
    "name":"Rajat Maharjan",
    "age":27,
    "class":"Programming",
    "Programming Language": ["Java", "Python", "C"]
    },
    {
    "name":"Ram Maharjan",
    "age":28,
    "class":"Programming",
    "Programming Language": ["Safe", "Cad", "Etabs"]
    },
{
    "name":"Raju Maharjan",
    "age":29,
    "class":"Programming",
    "Programming Language": ["SAFE", "Python", "ETABS"]
    }
]
userInput=input("Enter the name of program  for which you want to find the teacher: ")
for teacher in teacherArray:
    teacherName=teacher['name']
    teacherProgram=teacher['Programming Language']
    if userInput.capitalize() in teacherProgram:
        print(f'Only {teacherName} knows Python and other languages like {teacherProgram}')

print(type(teacher))
print(type(teacherName))
print(type(teacherProgram))
print("_______________")

#WAP to search database by user key and value:
teacherArrays=[
    {
    "name":"Rajat Maharjan",
    "username":"Rajat",
    "age":27,
    "class":"Programming",
    "Programming Language": ["Java", "Python", "C"],
    "grade":[1,2,3,4]
    },
    {
    "name":"Rajat Shrestha",
    "username":"Rajat",
    "age":28,
    "class":"Programming",
    "Programming Language": ["Safe", "Cad", "Etabs"],
    "grade":[11,12,13,14]
    },
{
    "name":"Raju Maharjan",
    "username":"Raju",
    "age":29,
    "class":"Programming",
    "Programming Language": ["Safe", "Python", "Etabs"],
    "grade":[10,1,13,2]
    }
]

userKey=""
userAllowInput=list(teacherArrays[1].keys())
print(userAllowInput)

for any in userAllowInput:
    if userKey not in userAllowInput:
        userKey=input("Enter the search parameter like name, username, age, class, Programming Language: ")
    else:
        break

print("___________________________________________________________________________")
userValue=input("Enter the value of that parameter to access the full database: ")
print("\n")

for userCompare in teacherArrays:
    if userKey=="age" or userKey=="grade":
        userValue=int(userValue)
    if userKey=="grade" or userKey=="Programming Language":
        if userValue in userCompare[userKey]:
            print(userCompare)
    else:
        if userCompare[userKey]== userValue:
            print(userCompare)
