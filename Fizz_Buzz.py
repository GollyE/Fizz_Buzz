# This is the FizzBuzz Program. The goal of this program is to cycle through a
# user defined ranged to determine those numbers that are
# evenly divisible by the number 3, the number, 5 or both.

my_input = input("Please the upper limit that you would like to count to in the Fizz Buzz Game:")
my_input = int(my_input)+1

for n in range(1,my_input):
    if(n % 5 == 0)and(n % 3 == 0):
        print("Fizz Buzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else: print(n)