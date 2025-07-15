import random

class Route:
    def __init__(self, cities, route = None):
        self.cities = cities
        self.route = route or self.generate_random_route()
        self.distance = None

    def generate_random_route(self):
        route = list(range(1, len(self.cities) + 1))
        random.shuffle(route) 
        return route

    def calculate_total_distance(self):
        total = 0
        for i in range(len(self.cities)-1):
            from_city = self.cities[self.route[i] - 1]
            to_city = self.cities[self.route[i+1] - 1]
            total += from_city.distance_to(to_city)
        total += self.cities[self.route[0] - 1].distance_to(self.cities[self.route[-1] - 1])
        return total
    
    