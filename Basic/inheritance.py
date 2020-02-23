class Vehicle:

    def __init__(self,name,color,value):
        self.name = name
        self.color = color
        self.value = value

class Truck(Vehicle):
    def __init__(self,name,color,value,available):
        super().__init__(name,color,value)
        self.available = available



volvo = Truck("volvo", "blue", 22.00, True)     
print(volvo.available)