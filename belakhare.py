import  pygame
class MyClass:
    number = 5
    string = "Hello!"
    def __init__(self, location):
        self.location_x = location[0]
        self.location_y = location[1]
    def change_location(self, amount):
        self.location_x += amount
        self.location_y += amount
        return  self.location_x, self.location_y
    def increment_number(self):
        MyClass.number += 1    