import math
from functools import lru_cache

class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        
    def distance_to(self, other_city):
        return self._calculate_distance(self.id, self.x, self.y, 
                                      other_city.id, other_city.x, other_city.y)
    
    @staticmethod
    @lru_cache(maxsize=None)  
    def _calculate_distance(id1, x1, y1, id2, x2, y2):
        if id1 > id2:
            id1, x1, y1, id2, x2, y2 = id2, x2, y2, id1, x1, y1
        
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    def __str__(self):
        return f"{self.id} - ({self.x},{self.y})"