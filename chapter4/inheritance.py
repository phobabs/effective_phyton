
# Inheritance
# # A class can inherit properties and methods from another class.

class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):  # Dog inherits from Animal
    def make_sound(self):
        return "Bark!"

dog = Dog("Canine")
print(dog.species)  # Canine
print(dog.make_sound())  # Bark!
