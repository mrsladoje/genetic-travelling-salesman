from models.route import Route

class Population:
    def __init__(self, cities, population_size):
        self.cities = cities
        self.population_size = population_size
        self.routes = []
        self.generation = 0
        self.best_distance_history = []
        self.avg_distance_history = []

    def initialize_population(self):
        self.routes= []
        for _ in range(self.population_size):
            route = Route(self.cities)
            self.routes.append(route)
        self.update_statistics()

    def update_statistics(self):
        distances = [route.distance for route in self.routes]
        self.best_distance_history.append(min(distances))
        self.avg_distance_history.append(sum(distances) / len(distances))
        
    def get_best_route(self):
        return min(self.routes, key=lambda x: x.distance)

    def get_worst_route(self):
        return max(self.routes, key=lambda x: x.distance)

    def sort_by_distance(self):
        self.routes.sort(key=lambda x: x.distance)