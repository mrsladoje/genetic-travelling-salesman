from models.city import City
from models.route import Route
from models.population import Population
from repository.reader import Reader

if __name__ == "__main__":
    reader = Reader()
    cities_data = reader.buffer_read()
    cities = [City(*map(float, line.split())) for line in cities_data]
    route = Route(cities)
    print("Cities:")
    for city in cities:
        print(city)
    print("Route")
    print(route.route)
    print(route.calculate_total_distance())

    print()
    population = Population(cities, 4)
    
    print("Testing Population Generation:")
    print(f"Population size: {population.population_size}")
    print(f"Initial routes count: {len(population.routes)}")
    
    population.initialize_population()
    
    print(f"After initialization - routes count: {len(population.routes)}")
    print(f"Generation: {population.generation}")
    
    for i, route in enumerate(population.routes):
        print(f"Route {i+1}: {route.route} - Distance: {route.distance}")
    
    print(f"\nBest distance history: {population.best_distance_history}")
    print(f"Average distance history: {population.avg_distance_history}")
    
    best_route = population.get_best_route()
    worst_route = population.get_worst_route()
    print(f"\nBest route: {best_route.route} - Distance: {best_route.distance}")
    print(f"Worst route: {worst_route.route} - Distance: {worst_route.distance}")
    
    print(f"\nBefore sorting:")
    for i, route in enumerate(population.routes):
        print(f"Route {i+1}: Distance {route.distance}")
    
    population.sort_by_distance()
    print(f"\nAfter sorting by distance:")
    for i, route in enumerate(population.routes):
        print(f"Route {i+1}: Distance {route.distance}")
    

    print("\nTesting Evolution:")
    population.evolve(mutation_rate=0.1, elite_size=2)
    print(f"After evolution - Generation: {population.generation}")
    print(f"Best route after evolution: {population.get_best_route().route} - Distance: {population.get_best_route().distance}")
    print(f"Worst route after evolution: {population.get_worst_route().route} - Distance: {population.get_worst_route().distance}")
    print(f"Average distance after evolution: {population.avg_distance_history[-1]}")
    print(f"Best distance after evolution: {population.best_distance_history[-1]}")
    print(f"Population size after evolution: {len(population.routes)}")
    print(f"Population routes after evolution:")
    for i, route in enumerate(population.routes):
        print(f"Route {i+1}: {route.route} - Distance: {route.distance}")
    print(f"\nBest route after evolution: {population.get_best_route().route} - Distance: {population.get_best_route().distance}")
    print(f"Worst route after evolution: {population.get_worst_route().route} - Distance: {population.get_worst_route().distance}")
    print(f"Average distance after evolution: {population.avg_distance_history[-1]}")
    print(f"Best distance after evolution: {population.best_distance_history[-1]}")
