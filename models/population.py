from models.route import Route
from genetic.selection import tournament_selection
from genetic.mutation import inversion_mutation
from genetic.crossover import partially_mapped_crossover

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

    def evolve(self, mutation_rate=0.1, elite_size=10):
        new_routes = []
        
        self.sort_by_distance()
        new_routes.extend(self.routes[:elite_size])
        
        while len(new_routes) < self.population_size:
            parent1 = tournament_selection(self)
            parent2 = tournament_selection(self)
            
            child = partially_mapped_crossover(parent1, parent2)
            child = inversion_mutation(child, mutation_rate)
            
            new_routes.append(child)
        
        self.routes = new_routes
        self.generation += 1
        self.update_statistics()
