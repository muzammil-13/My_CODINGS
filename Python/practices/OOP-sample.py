class Animal:  # Base class for inheritance
    def eat(self):
        print("I'm eating!")

class Dog(Animal):  # Inheritance
    species = "Canis familiaris"  # Class variable

    def __init__(self, name, breed):  # Constructor for instances
        self.name = name  # Instance variables
        self.breed = breed
        self.mood = "happy"  # Default mood

    def bark(self):  # Instance method
        print("Woof!")

    def describe(self):  # Instance method encapsulating data
        print(f"This is {self.name}, a {self.breed} dog.")

    def get_mood(self):  # Getter method for data protection
        return self.mood

    def set_mood(self, new_mood):  # Setter method for data protection
        self.mood = new_mood

    # Polymorphism example (overriding Animal's eat method)
    def eat(self):
        print(f"{self.name} is eating dog food!")

# Create two instances (objects) of the Dog class
my_dog = Dog("Fido", "Labrador")
your_dog = Dog("Buddy", "Golden Retriever")

# Access and modify attributes
print(my_dog.name)  # Access instance attribute
print(Dog.species)  # Access class variable
my_dog.species = "Canis lupus familiaris"  # Modify class variable (affects all dogs)

# Call instance methods
my_dog.bark()
my_dog.describe()

# Demonstrate encapsulation
print(my_dog.get_mood())  # Access mood through a method
my_dog.set_mood("sleepy")  # Change mood through a method

# Demonstrate polymorphism
my_dog.eat()  # Calls Dog's eat() method, not Animal's
your_dog.eat()  # Same for another dog instance
