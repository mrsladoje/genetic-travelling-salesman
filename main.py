from models.city import City
from models.route import Route
from models.population import Population

if __name__ == "__main__":
    cities = [City(1, 1, 1), City(2, 3, 1), City(3, 3, 3), City(4, 1, 3)]
    route = Route(cities)
    print("Cities: ", cities)
    print("Route")
    print(route.route)
    print(route.calculate_total_distance())

    print()
    population = Population(cities, 4)
    
    # Test population generation
    print("Testing Population Generation:")
    print(f"Population size: {population.population_size}")
    print(f"Initial routes count: {len(population.routes)}")
    
    # Initialize the population
    population.initialize_population()
    
    print(f"After initialization - routes count: {len(population.routes)}")
    print(f"Generation: {population.generation}")
    
    # Display each route in the population
    for i, route in enumerate(population.routes):
        print(f"Route {i+1}: {route.route} - Distance: {route.distance}")
    
    # Test statistics
    print(f"\nBest distance history: {population.best_distance_history}")
    print(f"Average distance history: {population.avg_distance_history}")
    
    # Test best and worst route methods
    best_route = population.get_best_route()
    worst_route = population.get_worst_route()
    print(f"\nBest route: {best_route.route} - Distance: {best_route.distance}")
    print(f"Worst route: {worst_route.route} - Distance: {worst_route.distance}")
    
    # Test sorting
    print(f"\nBefore sorting:")
    for i, route in enumerate(population.routes):
        print(f"Route {i+1}: Distance {route.distance}")
    
    population.sort_by_distance()
    print(f"\nAfter sorting by distance:")
    for i, route in enumerate(population.routes):
        print(f"Route {i+1}: Distance {route.distance}")