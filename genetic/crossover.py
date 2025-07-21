import random
from models.route import Route

def partially_mapped_crossover(parent1, parent2):
    route1 = parent1.route[:]
    route2 = parent2.route[:]
    
    start = random.randint(0, len(route1) - 2)
    end = random.randint(start + 1, len(route1))
    
    child_route = [-1] * len(route1)
    child_route[start:end] = route1[start:end]
    
    mapping = {}
    for i in range(start, end):
        mapping[route2[i]] = route1[i]
    
    for i in range(len(route1)):
        if child_route[i] == -1:
            candidate = route2[i]
            
            visited = set()  # Prevent infinite loops
            while candidate in mapping and candidate not in visited:
                visited.add(candidate)
                candidate = mapping[candidate]
            
            if candidate in child_route:
                for city_id in range(len(route1)):
                    if city_id not in child_route:
                        candidate = city_id
                        break
            
            child_route[i] = candidate
    
    child = Route(parent1.cities, child_route)
    return child