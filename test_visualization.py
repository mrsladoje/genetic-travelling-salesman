from models.city import City
from models.route import Route
from models.population import Population
from repository.reader import Reader
from visualizer import GeneticTSPVisualizer

def test_visualization():
    """Test visualization with current main.py structure"""
    print("Testing Genetic TSP Visualization")
    print("="*40)
    
    reader = Reader()
    cities_data = reader.buffer_read()
    cities = [City(*map(float, line.split())) for line in cities_data]
    
    print(f"Loaded {len(cities)} cities")
    
    population = Population(cities, 4)
    population.initialize_population()
    
    print(f"Created population with {len(population.routes)} routes")
    
    print("\nRunning a few evolution steps...")
    for i in range(5):
        population.evolve(mutation_rate=0.1, elite_size=2)
        print(f"Generation {i+1}: Best distance = {population.get_best_route().distance:.2f}")
    
    visualizer = GeneticTSPVisualizer(population, cities)
    
    print("\n" + "="*40)
    print("GENERATING VISUALIZATIONS")
    print("="*40)
    
    print("1. Cities distribution...")
    visualizer.plot_cities()
    
    print("2. Best route...")
    best_route = population.get_best_route()
    visualizer.plot_route(best_route, "Best Route")
    
    print("3. Population routes...")
    visualizer.plot_population_routes()
    
    print("4. Best vs worst comparison...")
    visualizer.plot_best_vs_worst()
    
    print("5. Distance distribution...")
    visualizer.plot_distance_distribution()
    
    print("6. Algorithm convergence...")
    visualizer.plot_convergence()
    
    print("\n7. Creating comprehensive report...")
    visualizer.create_comprehensive_report()
    
    print("\n" + "="*40)
    print("VISUALIZATION TEST COMPLETE!")
    print("Check the 'plots' directory for saved files.")
    print("="*40)

if __name__ == "__main__":
    test_visualization()
