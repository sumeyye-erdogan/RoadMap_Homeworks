# ABS Program

import math


def distance_from_zero(value):
    
    value_type = type(value)

    if value_type == int or value_type == float:
        return abs(value)
    else:
        return "Nope"


print(distance_from_zero(-5.6))
