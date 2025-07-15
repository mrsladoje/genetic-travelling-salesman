import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation
import os
from datetime import datetime

class GeneticTSPVisualizer:
    def __init__(self, population=None, cities=None):
        self.population = population
        self.cities = cities
        self.fig_size = (12, 8)
        
        plt.style.use('default')
        sns.set_palette("husl")
        
        if not os.path.exists('plots'):
            os.makedirs('plots')
    
    def plot_cities(self, title="Cities Distribution", save_path=None):
        """Plot all cities on a 2D map with labels"""
        fig, ax = plt.subplots(figsize=self.fig_size)
        
        if self.cities:
            x_coords = [city.x for city in self.cities]
            y_coords = [city.y for city in self.cities]
            city_ids = [int(city.id) for city in self.cities]
            
            scatter = ax.scatter(x_coords, y_coords, c='red', s=100, alpha=0.7, 
                               edgecolors='black', linewidth=2, zorder=3)
            
            for i, city_id in enumerate(city_ids):
                ax.annotate(f'{city_id}', (x_coords[i], y_coords[i]), 
                           xytext=(5, 5), textcoords='offset points', 
                           fontsize=8, fontweight='bold', color='black')
            
            ax.set_title(title, fontsize=16, fontweight='bold')
            ax.set_xlabel('X Coordinate', fontsize=12)
            ax.set_ylabel('Y Coordinate', fontsize=12)
            ax.grid(True, alpha=0.3)
            ax.set_aspect('equal')
            
            ax.text(0.02, 0.98, f'Total Cities: {len(self.cities)}', 
                   transform=ax.transAxes, verticalalignment='top',
                   bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
            
            plt.tight_layout()
            
            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
                print(f"Cities plot saved to: {save_path}")
            plt.show()
        else:
            print("No cities data available for plotting")
    
    def plot_route(self, route, title="Route Visualization", save_path=None):
        """Plot a specific route with cities and connections"""
        fig, ax = plt.subplots(figsize=self.fig_size)
        
        if route and route.route:
            route_cities = [self.cities[city_id - 1] for city_id in route.route]
            x_coords = [city.x for city in route_cities]
            y_coords = [city.y for city in route_cities]
            
            x_coords.append(x_coords[0])
            y_coords.append(y_coords[0])
            
            ax.plot(x_coords, y_coords, 'b-', linewidth=2, alpha=0.7, 
                   label=f'Route (Distance: {route.distance:.2f})')
            
            ax.scatter(x_coords[:-1], y_coords[:-1], c='red', s=100, alpha=0.8, 
                      edgecolors='black', linewidth=2, zorder=3)
            
            for i, city_id in enumerate(route.route):
                ax.annotate(f'{city_id}', (x_coords[i], y_coords[i]), 
                           xytext=(5, 5), textcoords='offset points', 
                           fontsize=8, fontweight='bold')
            
            ax.scatter(x_coords[0], y_coords[0], c='green', s=200, alpha=0.8, 
                      edgecolors='black', linewidth=3, label='Start/End', zorder=4)
            
            ax.set_title(f'{title}\nDistance: {route.distance:.2f}', 
                        fontsize=16, fontweight='bold')
            ax.set_xlabel('X Coordinate', fontsize=12)
            ax.set_ylabel('Y Coordinate', fontsize=12)
            ax.legend()
            ax.grid(True, alpha=0.3)
            ax.set_aspect('equal')
            
            plt.tight_layout()
            
            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
                print(f"Route plot saved to: {save_path}")
            plt.show()
        else:
            print("No route data available for plotting")
    
    def plot_population_routes(self, title="Population Routes", save_path=None):
        """Plot all routes in the current population"""
        if not self.population or not self.population.routes:
            print("No population data available for plotting")
            return
            
        fig, ax = plt.subplots(figsize=self.fig_size)
        
        colors = plt.cm.tab10(np.linspace(0, 1, len(self.population.routes)))
        
        for i, route in enumerate(self.population.routes):
            route_cities = [self.cities[city_id - 1] for city_id in route.route]
            x_coords = [city.x for city in route_cities]
            y_coords = [city.y for city in route_cities]
            
            x_coords.append(x_coords[0])
            y_coords.append(y_coords[0])
            
            ax.plot(x_coords, y_coords, color=colors[i], linewidth=1.5, alpha=0.7, 
                   label=f'Route {i+1} (Dist: {route.distance:.0f})')
        
        if self.cities:
            x_coords = [city.x for city in self.cities]
            y_coords = [city.y for city in self.cities]
            ax.scatter(x_coords, y_coords, c='red', s=60, alpha=0.8, 
                      edgecolors='black', linewidth=1, zorder=3)
        
        ax.set_title(f'{title} (Generation {self.population.generation})', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('X Coordinate', fontsize=12)
        ax.set_ylabel('Y Coordinate', fontsize=12)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(True, alpha=0.3)
        ax.set_aspect('equal')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Population routes plot saved to: {save_path}")
        plt.show()
    
    def plot_convergence(self, title="Algorithm Convergence", save_path=None):
        """Plot convergence of best and average distances over generations"""
        if not self.population or not self.population.best_distance_history:
            print("No convergence data available for plotting")
            return
            
        fig, ax = plt.subplots(figsize=self.fig_size)
        
        generations = range(len(self.population.best_distance_history))
        
        ax.plot(generations, self.population.best_distance_history, 'g-', 
               linewidth=2, marker='o', markersize=4, label='Best Distance')
        
        if self.population.avg_distance_history:
            ax.plot(generations, self.population.avg_distance_history, 'b--', 
                   linewidth=2, marker='s', markersize=4, label='Average Distance')
        
        ax.set_title(title, fontsize=16, fontweight='bold')
        ax.set_xlabel('Generation', fontsize=12)
        ax.set_ylabel('Distance', fontsize=12)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        if len(self.population.best_distance_history) > 1:
            initial_best = self.population.best_distance_history[0]
            final_best = self.population.best_distance_history[-1]
            improvement = ((initial_best - final_best) / initial_best) * 100
            
            ax.text(0.02, 0.98, f'Improvement: {improvement:.1f}%\nFinal Best: {final_best:.2f}', 
                   transform=ax.transAxes, verticalalignment='top',
                   bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Convergence plot saved to: {save_path}")
        plt.show()
    
    def plot_distance_distribution(self, title="Distance Distribution", save_path=None):
        """Plot distribution of distances in current population"""
        if not self.population or not self.population.routes:
            print("No population data available for plotting")
            return
            
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        distances = [route.distance for route in self.population.routes]
        
        ax1.hist(distances, bins=min(10, len(distances)), alpha=0.7, 
                color='skyblue', edgecolor='black')
        ax1.set_title('Distance Distribution', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Distance', fontsize=12)
        ax1.set_ylabel('Frequency', fontsize=12)
        ax1.grid(True, alpha=0.3)
        
        bp = ax2.boxplot(distances, patch_artist=True)
        bp['boxes'][0].set_facecolor('lightcoral')
        bp['boxes'][0].set_alpha(0.7)
        ax2.set_title('Distance Statistics', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Distance', fontsize=12)
        ax2.grid(True, alpha=0.3)
        
        stats_text = (f'Min: {min(distances):.2f}\n'
                     f'Max: {max(distances):.2f}\n'
                     f'Mean: {np.mean(distances):.2f}\n'
                     f'Std: {np.std(distances):.2f}')
        ax2.text(1.1, 0.5, stats_text, transform=ax2.transAxes, 
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
        
        plt.suptitle(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Distance distribution plot saved to: {save_path}")
        plt.show()
    
    def plot_best_vs_worst(self, title="Best vs Worst Routes", save_path=None):
        """Compare best and worst routes side by side"""
        if not self.population or not self.population.routes:
            print("No population data available for plotting")
            return
            
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
        
        best_route = self.population.get_best_route()
        worst_route = self.population.get_worst_route()
        
        self._plot_single_route(ax1, best_route, 'Best Route', 'green')
        
        self._plot_single_route(ax2, worst_route, 'Worst Route', 'red')
        
        plt.suptitle(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Best vs worst routes plot saved to: {save_path}")
        plt.show()
    
    def _plot_single_route(self, ax, route, title, color):
        """Helper method to plot a single route on given axes"""
        if route and route.route:
            route_cities = [self.cities[city_id - 1] for city_id in route.route]
            x_coords = [city.x for city in route_cities]
            y_coords = [city.y for city in route_cities]
            
            x_coords.append(x_coords[0])
            y_coords.append(y_coords[0])
            
            ax.plot(x_coords, y_coords, color=color, linewidth=2, alpha=0.7)
            
            ax.scatter(x_coords[:-1], y_coords[:-1], c='blue', s=80, alpha=0.8, 
                      edgecolors='black', linewidth=1, zorder=3)
            
            for i, city_id in enumerate(route.route):
                ax.annotate(f'{city_id}', (x_coords[i], y_coords[i]), 
                           xytext=(3, 3), textcoords='offset points', 
                           fontsize=8, fontweight='bold')
            
            ax.scatter(x_coords[0], y_coords[0], c='orange', s=150, alpha=0.8, 
                      edgecolors='black', linewidth=2, zorder=4)
            
            ax.set_title(f'{title}\nDistance: {route.distance:.2f}', 
                        fontsize=14, fontweight='bold')
            ax.set_xlabel('X Coordinate', fontsize=12)
            ax.set_ylabel('Y Coordinate', fontsize=12)
            ax.grid(True, alpha=0.3)
            ax.set_aspect('equal')
    
    def plot_evolution_progress(self, generations_data, title="Evolution Progress", save_path=None):
        """Plot multiple generations to show evolution progress"""
        if not generations_data:
            print("No evolution data available for plotting")
            return
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        axes = axes.flatten()
        
        selected_generations = [0, len(generations_data)//3, 2*len(generations_data)//3, len(generations_data)-1]
        
        for i, gen_idx in enumerate(selected_generations):
            if gen_idx < len(generations_data):
                generation_data = generations_data[gen_idx]
                best_route = generation_data['best_route']
                
                self._plot_single_route(axes[i], best_route, 
                                      f'Generation {gen_idx} (Best)', 'blue')
        
        plt.suptitle(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Evolution progress plot saved to: {save_path}")
        plt.show()
    
    def create_comprehensive_report(self, save_dir='plots'):
        """Create a comprehensive visualization report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_dir = os.path.join(save_dir, f'tsp_report_{timestamp}')
        
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
        
        print(f"Creating comprehensive visualization report in: {report_dir}")
        print("="*60)
        
        print("1. Generating cities distribution plot...")
        self.plot_cities(save_path=os.path.join(report_dir, '1_cities_distribution.png'))
        
        if self.population and self.population.routes:
            print("2. Generating population routes plot...")
            self.plot_population_routes(save_path=os.path.join(report_dir, '2_population_routes.png'))
            
            print("3. Generating best vs worst routes plot...")
            self.plot_best_vs_worst(save_path=os.path.join(report_dir, '3_best_vs_worst.png'))
            
            print("4. Generating distance distribution plot...")
            self.plot_distance_distribution(save_path=os.path.join(report_dir, '4_distance_distribution.png'))
            
            print("5. Generating best route plot...")
            best_route = self.population.get_best_route()
            self.plot_route(best_route, "Best Route", 
                          save_path=os.path.join(report_dir, '5_best_route.png'))
        
        if (self.population and self.population.best_distance_history and 
            len(self.population.best_distance_history) > 1):
            print("6. Generating convergence plot...")
            self.plot_convergence(save_path=os.path.join(report_dir, '6_convergence.png'))
        
        print("="*60)
        print(f"Comprehensive report generated in: {report_dir}")
        print("="*60)
    
    def show_all_plots(self):
        """Display all available plots interactively"""
        print("Displaying all visualization plots...")
        print("="*50)
        
        print("1. Cities Distribution")
        self.plot_cities()
        
        if self.population and self.population.routes:
            print("2. Population Routes")
            self.plot_population_routes()
            
            print("3. Best vs Worst Routes")
            self.plot_best_vs_worst()
            
            print("4. Distance Distribution")
            self.plot_distance_distribution()
            
            print("5. Best Route")
            best_route = self.population.get_best_route()
            self.plot_route(best_route, "Best Route")
            
            if (self.population.best_distance_history and 
                len(self.population.best_distance_history) > 1):
                print("6. Algorithm Convergence")
                self.plot_convergence()
        
        print("="*50)
        print("All plots displayed")


def create_evolution_visualization(cities, population_size=20, generations=50, 
                                 mutation_rate=0.1, elite_size=2):
    """Run evolution and create comprehensive visualization"""
    from models.population import Population
    
    print(f"Running evolution with visualization...")
    print(f"Population: {population_size}, Generations: {generations}")
    print("="*60)
    
    population = Population(cities, population_size)
    population.initialize_population()
    
    generations_data = []
    
    print(f"Generation 0 - Best: {population.get_best_route().distance:.2f}")
    
    for generation in range(generations):
        population.evolve(mutation_rate=mutation_rate, elite_size=elite_size)
        
        generations_data.append({
            'generation': generation + 1,
            'best_route': population.get_best_route(),
            'best_distance': population.get_best_route().distance,
            'avg_distance': population.avg_distance_history[-1]
        })
        
        if generation % 10 == 0 or generation == generations - 1:
            best_distance = population.get_best_route().distance
            avg_distance = population.avg_distance_history[-1]
            print(f"Generation {population.generation} - Best: {best_distance:.2f}, Avg: {avg_distance:.2f}")
    
    print("="*60)
    print("Evolution complete!")
    print(f"Final Best Distance: {population.get_best_route().distance:.2f}")
    print("="*60)
    
    visualizer = GeneticTSPVisualizer(population, cities)
    visualizer.create_comprehensive_report()
    
    return population, visualizer, generations_data
