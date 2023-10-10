#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

lastdig = number % 10

str1 = "Last digit of {} is {} and is {}"
if (lastdig > 5):
    print(str1.format(number, lastdig, "greater than 5"))
elif (lastdig == 0):
    print(str1.format(number, lastdig, "0"))
elif (lastdig < 6 and lastdig != 0):
    print(str1.format(number, lastdig, "less than 6 and not 0"))
