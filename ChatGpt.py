class Animal:
    def __init__(self, name):
        self.name = name

    def make_sounds(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Create instances of subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Access methods from superclass
print(dog.name)          # Output: Buddy
print(cat.make_sounds())  # Output: Meow

# Access overridden method in subclasses
print(dog.make_sound())  # Output: Woof! Woof!
print(cat.make_sound())  # Output: Meow
