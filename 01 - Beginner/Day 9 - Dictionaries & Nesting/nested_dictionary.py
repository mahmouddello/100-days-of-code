# Nesting

capitals = {"France": "Paris",
            "Germany": "Berlin"
            }

# Nesting a list in a Dictionary

travel_log = {"France": ["Paris", "Lille", "Dijon"],
              "Germany": ["Berlin", "Frankfurt", "Hamburg"]
              }
# we can't save more than one value in a single key that's the reason why we used a list


# Nesting a Dictionary in a Dictionary


travel_log2 = {"France": {"cities visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
               "Germany": {"cities visited": ["Berlin", "Frankfurt", "Hamburg"], "total_visits": 15}
               }
# cities_visited is a dictionary


# Nesting a Dictionary in a list

travel_log3 = [
    {
        "country": "France",
        "cities visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities visited": ["Berlin", "Frankfurt", "Hamburg"],
        "total_visits": 15
    }
]
