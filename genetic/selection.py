import random

def tournament_selection(population, tournament_size=5):
    """Tournament selection - chooses the best route from a random selection"""
    tournament = random.sample(population.routes, tournament_size)
    return min(tournament, key=lambda x: x.get_distance())
