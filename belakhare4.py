import  pygame
class MyClass:
    number = 5
    string = "Hello!"
    def __init__(self,location):
        self.location_x = location[0]
        self.location_y = location[1]
    def change_location(self, amount):
        self.location_x += amount
        self.location_y += amount
    def increment_number(self):
        MyClass.number += 1   
    def pending_functionality(self):
       pass 
class Alien:
    total_aliens_created=0
    xl=0
    def __init__(self,location):
        self.health=3
        Alien.total_aliens_created+=1
        self.x_coordinate=location[0]
        self.y_coordinate=location[1]
    def hit(self):
        self.health-=1
    def is_alive(self):
        if (self.health<=0):
            return "False"
        else :
            return "True"
    def teleport(self,x,y):
        self.x_coordinate=x
        self.y_coordinate=y

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
             

