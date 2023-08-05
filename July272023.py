# multiplication table howework
for row in range(1, 13):
    for column in range(1, 11):
        print(f'{row}x{column}={row * column}')

# WAP double loop using While
floor = 1
while floor < 3:
    classe = 1
    while classe < 5:
        print(f'{floor},{classe}')
        classe = classe + 1
    floor = floor + 1

# Wap to find all combinations of value1 and value 2
value1 = [1, 2, 4, 5, 6]
value2 = [2, 4, 6, 8, 10]
for val1 in value1:
    for val2 in value2:
        print(f'{val1},{val2}')

myArray = [
    ["Ram", "Shyam", "Hari", "Gopal"],
    ["Radhe", "Sita", "Geeta", "Reeta", "abc"]
]
for x in range(0, len(myArray)):
    newArray = myArray[x]
    for y in range(0, len(newArray)):
        print(myArray[x][y])

for x in myArray:
    for y in x:
        print(y)

# Separate name with odd and even len in two different list:
newEvenArray = []
newOddArray = []
for x in myArray:
    for y in x:
        if len(y) % 2 == 0:
            newEvenArray.append(y)
        else:
            newOddArray.append(y)
print(f'For odd {newOddArray}')
print(f'For even {newEvenArray}')

# WAP
teacherArray = [
    {
        "name": "Prayush Shrestha",
        "username": "prayush",
        "age": 27,
        "class": "Python Programming",
        "Programming Languages": ["Java", "Python", "JS"],
        'Marks': [70, 89, 90, 91]
    },
    {
        "name": "Aayush Shrestha",
        "age": 31,
        "username": "ayush",
        "class": "Java Programming",
        "Programming Languages": ["Java", "Swift", "JS"],
        'Marks': [88, 89, 90, 91]
    },
    {
        "name": "Rita Shrestha",
        "age": 25,
        "married": "False",
        "username": "rita",
        "class": "UI UX",
        "Programming Languages": ["HTML", "CSS", "JS"],
        'Marks': [70, 89, 90, 91]
    },
    {
        "name": "Aayusha Pokharel",
        "age": 22,
        "username": "aayusha",
        "class": "Java Programming",
        "Programming Languages": ["Python", "Dart"],
        'Marks': [80, 89, 92, 91]
    }

]
highest = 0
highestname = ""
for first in teacherArray:
    obtainValue = 0
    var = first["Marks"]
    for marks in var:
        obtainValue += marks
    percent = (obtainValue / 4)
    if highest < percent:
        highest = percent
        highestname = first["name"]
    print(f'{first.get("name")} has got a percent of {percent}')
print("_________________")
print(f'Highest percent is {highest} and obtained by {highestname}')
