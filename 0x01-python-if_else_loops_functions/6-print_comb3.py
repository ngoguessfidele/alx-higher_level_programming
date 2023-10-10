#!/usr/bin/python3

for num in range(0, 100):
    if ((num / 10 != num % 10) and (num / 10 < num % 10)):
        print("{}{}".format(int(num / 10), num % 10), end="")
        if (num != 89):
            print(", ", end="")
else:
    print("")
