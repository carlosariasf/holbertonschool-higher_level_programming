#!/usr/bin/python3
def fizzbuzz():
    for c in range(101):
        if (c % 3) != 0 and (c % 5) != 0:
            print("{} ".format(c), end="")
        elif (c % 3) == 0 and (c % 5) == 0 and c > 0:
            print("FizzBuzz ", end="")
        elif (c % 3) == 0 and c > 0:
            print("Fizz ", end="")
        elif (c % 5) == 0 and c > 0 and c < 100:
            print("Buzz ", end="")
    print("Buzz ", end="")
