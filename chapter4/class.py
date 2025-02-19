#Defining a Class
#A class is created using the class keyword. Here's a simple example:

class Person:
    def __init__(self, name, age):  # Constructor (initializes object attributes)
        self.name = name
        self.age = age

    def greet(self):  # A method (function inside a class)
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an object (instance of the class)
person1 = Person("Alice", 25)

# Calling a method
print(person1.greet())  # Output: Hello, my name is Alice and I am 25 years old.


# Class vs. Instance Variables
# Class Variables: Shared across all instances.
# Instance Variables: Unique to each object.

class Dog:
    species = "Canine"  # Class variable (same for all dogs)

    def __init__(self, name):
        self.name = name  # Instance variable (unique to each dog)

dog1 = Dog("Buddy")
dog2 = Dog("Rocky")

print(dog1.species)  # Canine
print(dog2.species)  # Canine
print(dog1.name)  # Buddy
print(dog2.name)  # Rocky
