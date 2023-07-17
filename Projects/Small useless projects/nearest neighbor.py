import math

def nearest_neighbor(start_city, cities):
    visited_cities = [start_city]
    path = [start_city]
    while len(visited_cities) < len(cities):
        nearest_city = None
        nearest_distance = float('inf')
        for city in cities:
            if city[0] not in visited_cities:
                distance = city[1]
                if distance < nearest_distance:
                    nearest_city = city[0]
                    nearest_distance = distance
        visited_cities.append(nearest_city)
        path.append(nearest_city)
    return path

# Example usage
cities = [('lebanon',1000),('New York', 100), ('Boston', 75), ('Chicago', 300), ('Los Angeles', 500)]
start_city = 'lebanon'
path = nearest_neighbor(start_city, cities)
print(path)
