from models.city import City
from models.route import Route
from models.population import Population
from repository.reader import Reader

if __name__ == "__main__":
    reader = Reader()
    cities_data = reader.buffer_read()
    cities = [City(*map(float, line.split())) for line in cities_data]
    route = Route(cities)

    print()
    population = Population(cities, 100)
    
    print("Testing Population Generation:")
    print(f"Population size: {population.population_size}")
    print(f"Initial routes count: {len(population.routes)}")
    
    population.initialize_population()
    
    population.sort_by_distance()
    print(f"Initial best distance: {population.best_distance_history[0]:.2f}")
    print(f"Initial average distance: {population.avg_distance_history[0]:.2f}")
    print()
    
    # Run evolution for multiple generations
    num_generations = 500
    for generation in range(num_generations):
        population.evolve(mutation_rate=0.1, elite_size=10)
        
        # Print progress every 10 generations
        if (generation + 1) % 10 == 0:
            print(f"Generation {population.generation}: "
                  f"Best = {population.best_distance_history[-1]:.2f}, "
                  f"Average = {population.avg_distance_history[-1]:.2f}")
    
    print()
    print("=== FINAL RESULTS ===")
    print(f"Final Generation: {population.generation}")
    print(f"Best distance: {population.best_distance_history[-1]:.2f}")
    print(f"Average distance: {population.avg_distance_history[-1]:.2f}")
    print(f"Improvement: {population.best_distance_history[0] - population.best_distance_history[-1]:.2f}")
    print(f"Best route: {population.get_best_route().route}")
