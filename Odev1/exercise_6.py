# Cube Program

import math


def cube(s):
    return pow(s, 3)


def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False


check = int(input("Sayı giriniz: "))

print(by_three(check))


