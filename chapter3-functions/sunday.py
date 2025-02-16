#from pydantic import BaseModel

def greet(name: str) -> None:
   # print("Hello, " + name + "!")

    greet('Omotolani') # Hello, Omotolani!

def add(a: int, b: int) -> int:
    return a + b

# print(add(2, 3)) # 5


# class concept in python

class Microwave:
    # prototype of the class, the word self is just an instance of that class..blue print o fthe class
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.turn_on= False

# Methods in python
# Methods are functions that are defined inside a class.
# They are used to define the behaviors of an object. We have created an object for example microwave
# and we can define a method that will be used to turn on the microwave or ask the microwave to do something

    def turn_on(self) -> None:
        if self.turned_on:
            print(f'The {self.brand} microwave is already on')
        else:
            self.turned_on = True
            print(f'The {self.brand} microwave is on')
        
      
    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f'The {self.brand} microwave is now turned off.')
        else:
            print(f'The {self.brand} microwave is turned off') 
            
    def run(self, seconds: int) -> None:    
        if self.turned_on: 
            print(f'The {self.brand} microwave is running for {seconds} seconds')
        else:
            print(f'The {self.brand} microwave should be turn on first before running')   
                  


bosch: Microwave = Microwave('Bosch', 'Y1', 2022) 
bosch.turn_on() # The Bosch microwave is on
bosch.run(30) # The Bosch microwave is running for 30 seconds
bosch.turn_off() # The Bosch microwave is now turned off
bosch.run(10) # The Bosch microwave should be turn on first before running
print(bosch.brand,bosch.model,bosch.year,bosch.turn_on()) # Bosch        
               

class Car:
    def __init__(self, brand: str, horsepower: int, year: int) -> None:
        self.brand = brand
        self.horsepower = horsepower
        self.year = year
        
    def drive(self) -> None:
        print(f'The {self.brand} car is driving')
    
    def get_info(self) -> None:
        print(f'The {self.year} {self.brand} has {self.horsepower} horsepower')
        
        # Dunder method will be used to return a string representation of the object
    def __str__(self) -> str:
        return f'{self.brand, self.brand,self.year} car'    
        
volvo: Car = Car('Volvo', 200, 2021)
Benz: Car = Car('Benz', 300, 2022)
print(volvo.drive()) # The 2021 Volvo has 200 horsepower

# Dunder(double underscore) methods in python

volvo: Car = Car('Volvo', 200, 2021)
# this will return an object of the class Car   
print(volvo)# <__main__.Car object at 0x7f8b3c1b3d30>
# but the output is not very useful.    
# to make it more useful, you can define a __str__ method in the class Car

# concept of polymorphism in python
# Polymorphism is the ability to define a single interface and have multiple implementations.
    


    
    
    
    
    

        
                    
                    



 