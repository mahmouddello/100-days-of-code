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


# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇

def add_new_country(the_country, visit_amount, cities_list):
    # Angela's solution :
    # new_country = {}
    # new_country ["country"] = the_country >> 'country' : key , 'the_country' parameter is the value
    # new_country ["visits"] = visit_amount >> 'visits' : key , 'visit_amount' parameter is the value
    # new_country ["cities"] = cities_list >> 'cities' : key , 'cities_list' list parameter is the value

    # my solution
    new_dictionary = {"country": the_country, "visits": visit_amount, "cities": cities_list}
    travel_log.append(new_dictionary)


# 🚨 Do not change the code below
add_new_country(the_country="Russia", visit_amount=2, cities_list=["Moscow", "Saint Petersburg"])
print(travel_log)
