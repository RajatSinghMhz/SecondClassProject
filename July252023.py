#WAP to above dictionary calculate the heights marks and also percentage obtained assuming total of all subject is 100//
myMarks={
    "maths":10,
    "science":100,
    "english":50,
    "sanskrit":80,
    "nepali":70
}
print(myMarks.keys())               #keys le key return garxa// can be used to assign into list// 2D element bata 1D banaune trick//
print(myMarks.values())             #Values le value return garxa//
print(myMarks.items())              #items le tuple return garxa//
print(list(myMarks.items()))        #Typecaste gareko list ma//
totalMarks=len(myMarks)*100         #Len function list ma paincha// sort pani cha list ma// list is very useful//
print(totalMarks)
marksOnly=list(myMarks.values())    #TypeCast gareko
marksOnly.sort()
highestMark=marksOnly[-1]

print("______________________________________")
totalObtained=0
for marks in marksOnly:
    totalObtained=totalObtained+marks
percentage=(totalObtained/totalMarks)*100
print(f'The total percentage is {percentage}')
print("______________________________________")

#Find a program to print "Python"
studentDictionary={
    "name":"Rajat Maharjan",
    "age":27,
    "class":"Programming",
    "Programming Language":["Java","Python","C"],
    "grades":[11,12,18,9]
}
print(studentDictionary["Programming Language"][1])
gradeList=studentDictionary["grades"]
gradeList.sort()
print(gradeList[-1])
print("______________________________________")

#WAP to find CAD
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
    "Programming Language": ["SAFE", "CAD", "ETABS"]
    }
]
print(teacherArray[1]["name"])
print(teacherArray[1]["Programming Language"][1])
print("______________________________________")

#Create a list containing 5 students with marks and grade and subjects (array) and display all the students with "Python" as subject//
studentArray=[
    {
    "name":"Rajat Maharjan",
    "marks":99,
    "class":"Python"
    },
    {
    "name":"Anjan Maharjan",
    "marks":98,
    "class":"Python"
    },
    {
    "name":"Raj Maharjan",
    "marks":95,
    "class":"Science"
    },
    {
    "name":"RamMaharjan",
    "marks":97,
    "class":"CAD"
    },
    {
    "name":"Raja Maharjan",
    "marks":99,
    "class":"Biology"
    }
]
x=len(studentArray)
for val in range(0,x):
    if studentArray[val]["class"]=="Python":
        print(studentArray[val]["name"])
print("______________________________________")
matrixList=[
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        ["a","b","c"],
        ["d","e","f"],
        ["g","h","i"]
    ],
    [
        [11,12,13],
        [14,15,16],
        [17,18,19]
    ]
]
print(matrixList[1])
print("______________________________________")

# 2D Dictionary
matrix_dict = {
    (0, 0): 1, (0, 1): 2, (0, 2): 3,
    (1, 0): 4, (1, 1): 5, (1, 2): 6,
    (2, 0): 7, (2, 1): 8, (2, 2): 9
}
print(matrix_dict.values())
print("______________________________________")

# 3D Dictionary
cube_dict = {
    (0, 0, 0): 1, (0, 0, 1): 2, (0, 0, 2): 3,
    (0, 1, 0): 4, (0, 1, 1): 5, (0, 1, 2): 6,
    (0, 2, 0): 7, (0, 2, 1): 8, (0, 2, 2): 9,
    (1, 0, 0): 10, (1, 0, 1): 11, (1, 0, 2): 12,
    (1, 1, 0): 13, (1, 1, 1): 14, (1, 1, 2): 15,
    (1, 2, 0): 16, (1, 2, 1): 17, (1, 2, 2): 18,
    (2, 0, 0): 19, (2, 0, 1): 20, (2, 0, 2): 21,
    (2, 1, 0): 22, (2, 1, 1): 23, (2, 1, 2): 24,
    (2, 2, 0): 25, (2, 2, 1): 26, (2, 2, 2): 27
}
print(cube_dict.values())
print("______________________________________")