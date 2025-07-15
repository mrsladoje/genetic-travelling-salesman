import random
from models.route import Route

def inversion_mutation(route, mutation_rate=0.1):
    if random.random() < mutation_rate:
        mutated_route = route.route[:]
        start = random.randint(0, len(mutated_route) - 2)
        end = random.randint(start + 1, len(mutated_route))
        
        # Obrni segment
        mutated_route[start:end] = reversed(mutated_route[start:end])
        
        new_route = Route(route.cities, mutated_route)
        return new_route
    return route