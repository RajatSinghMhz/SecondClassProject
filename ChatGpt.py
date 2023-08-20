class Individual:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, of age {self.age}"


class Employee(Individual):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        return super().__str__() + f", Grade is {self.grade}"


class Instructor(Individual):
    def __init__(self, name, age, topic):
        super().__init__(name, age)
        self.topic = topic

    def __str__(self):
        return super().__str__() + f", instructs: {self.topic}"


class MarkingCriteria:
    def __init__(self, criteria, instructor, employee):
        self.criteria = criteria
        self.employee = employee
        self.instructor = instructor

    def __str__(self):
        return f"{self.criteria} evaluated by {self.instructor} for employee {self.employee} "

employee1 = Employee("Rajat", 27, "A+")
employee2 = Employee("Zenith", 30, "B+")

instructor1 = Instructor("Prakash G", 35, "Etabs")
instructor2 = Instructor("Prayush S", 32, "Python")

markingCriteria1 = MarkingCriteria("Expertise and Speed", instructor1, [employee1, employee2])
markingCriteria2 = MarkingCriteria("Logic and Accuracy", instructor2, employee1)

print(markingCriteria1)
print(markingCriteria2)
