# Public Variables (No Encapsulation)
# By default, all class attributes are public, meaning 
# they can be accessed and modified directly.

class Car:
    def __init__(self, brand, speed):
        self.brand = brand  # Public attribute
        self.speed = speed  # Public attribute

car = Car("Toyota", 120)
print(car.brand)  # ✅ Toyota (Accessible)
car.speed = 150   # ✅ Can modify directly
print(car.speed)  # 150
# In the above example, brand and speed are public attributes of the Car class.