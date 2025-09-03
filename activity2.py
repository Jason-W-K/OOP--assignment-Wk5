# 🚗 Base class with polymorphic method
class Vehicle:
    def move(self):
        return "The vehicle moves forward."

# 🚙 Subclass: Car
class Car(Vehicle):
    def move(self):
        return "Driving on the highway 🚗"

# ✈️ Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying through the clouds ✈️"

# 🚲 Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        return "Pedaling down the lane 🚲"

# 🚀 Subclass: Rocket
class Rocket(Vehicle):
    def move(self):
        return "Launching into space 🚀"

# 🧪 Test polymorphism
vehicles = [Car(), Plane(), Bicycle(), Rocket()]

for v in vehicles:
    print(v.move())
