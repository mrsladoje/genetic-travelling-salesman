import math 

class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        
    def distance_to(self, other_city):
        return math.sqrt((self.x-other_city.x)**2 + (self.y-other_city.y)**2)
    
    def __str__(self):
        return f"{self.id} - ({self.x},{self.y})"

        