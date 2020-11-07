# Calculate trip's costs


def hotel_cost(night_count):
    return 140 * night_count


def plane_ride_cost(city):
    switcher = {
        "Charlotte": 183,
        "Tampa": 220,
        "Pittsburgh": 222,
        "Los Angeles": 475
    }
    return switcher.get(city)


def rental_car_cost(days):
    cost = 40 * days
    
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost


def trip_cost(city, days, spending_money):
    return hotel_cost(days) + rental_car_cost(days) + plane_ride_cost(city) + spending_money


print(trip_cost("Charlotte", 10, 500))
