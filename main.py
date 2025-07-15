from models.city import City
from models.route import Route

if __name__ == "__main__":
    cities = [City(1, 1, 1), City(2, 3, 1), City(3, 3, 3), City(4, 1, 3)]
    route = Route(cities)
    print("Cities: ", cities)
    print("Route")
    print(route.route)
    print(route.calculate_total_distance())