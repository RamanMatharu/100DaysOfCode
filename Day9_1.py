# travel_log

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

country = input("Write the country name you visited:")
no_of_visits = int(input("How many times have you visited there? "))
cities = []

# count = int(input("How many cities have you visited? "))
visited_cities = input("Add the name of cities you visited: ")
cities = visited_cities.split(', ')

travelled_city = {}


def add_new_country(country_name, visits, cities_visited):
    travelled_city["country"] = country_name
    travelled_city["visits"] = visits
    travelled_city["cities"] = cities_visited
    travel_log.append(travelled_city)


add_new_country(country, no_of_visits, cities)
print(travel_log)
