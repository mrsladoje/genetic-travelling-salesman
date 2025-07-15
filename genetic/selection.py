import random

def tournament_selection(population, tournament_size=5):
    """Tournament selection - chooses the best route from a random selection"""
    # Ensure tournament size doesn't exceed population size
    actual_tournament_size = min(tournament_size, len(population.routes))
    tournament = random.sample(population.routes, actual_tournament_size)
    return min(tournament, key=lambda x: x.distance)
