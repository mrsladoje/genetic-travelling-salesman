from models.city import City
from models.route import Route
from models.population import Population
from repository.reader import Reader
from visualizer import GeneticTSPVisualizer, create_evolution_visualization

def main():
    print("="*60)
    print("GENETIC TRAVELING SALESMAN ALGORITHM")
    print("="*60)
    
    reader = Reader()
    cities_data = reader.buffer_read()
    cities = [City(*map(float, line.split())) for line in cities_data]
    
    print(f"Loaded {len(cities)} cities")
    
    population = Population(cities, 4)
    population.initialize_population()
    
    print("\n" + "="*60)
    print("BASIC TESTING")
    print("="*60)
    
    print(f"Population size: {population.population_size}")
    print(f"Generation: {population.generation}")
    
    print("\nInitial Population Routes:")
    for i, route in enumerate(population.routes):
        print(f"Route {i+1}: Distance {route.distance:.2f}")
    
    best_route = population.get_best_route()
    worst_route = population.get_worst_route()
    print(f"\nBest route distance: {best_route.distance:.2f}")
    print(f"Worst route distance: {worst_route.distance:.2f}")
    
    print("\nTesting Evolution...")
    population.evolve(mutation_rate=0.1, elite_size=2)
    print(f"After 1 generation - Best: {population.get_best_route().distance:.2f}")
    
    print("\n" + "="*60)
    print("VISUALIZATION")
    print("="*60)
    
    visualizer = GeneticTSPVisualizer(population, cities)
    
    print("Displaying basic visualizations...")
    visualizer.show_all_plots()
    
    print("\nGenerating comprehensive report...")
    visualizer.create_comprehensive_report()
    
    print("\n" + "="*60)
    print("FULL EVOLUTION WITH VISUALIZATION")
    print("="*60)
    
    final_population, final_visualizer, generations_data = create_evolution_visualization(
        cities=cities,
        population_size=30,
        generations=100,
        mutation_rate=0.1,
        elite_size=3
    )
    
    print(f"\n✓ Evolution complete!")
    print(f"Final best distance: {final_population.get_best_route().distance:.2f}")
    print(f"Initial best distance: {final_population.best_distance_history[0]:.2f}")
    
    improvement = ((final_population.best_distance_history[0] - final_population.get_best_route().distance) / 
                   final_population.best_distance_history[0]) * 100
    print(f"Improvement: {improvement:.1f}%")
    
    print("\n" + "="*60)
    print("PROGRAM COMPLETE")
    print("Check the 'plots' directory for saved visualizations!")
    print("="*60)

if __name__ == "__main__":
    main()
