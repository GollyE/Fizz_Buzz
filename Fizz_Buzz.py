# This is the FizzBuzz Program. The goal of this program is to cycle through a
# user defined ranged to determine those numbers that are
# evenly divisible by the number 3, the number, 5 or both.

Test = True
my_input= int()
my_input = input("Please the upper limit that you would like to count to in the Fizz Buzz Game:")
while Test: # Check to determine if the user entered an integer, accounts for multiple incorrect entries
    Pass = True  
    try:
        my_input = int(my_input)
    except ValueError:
        print("Please enter a number in integer format using the number keys on your keyboard")
        my_input = input("Please the upper limit that you would like to count to in the Fizz Buzz Game:")
        Pass = False # flags the entry for another check, just in case the user didn't catch the whole integer thing
    if Pass == True: # check to determine if we have an integer and can exit loop
        Test = False
my_input = int(my_input)+1


for n in range(1,my_input):
    if(n % 5 == 0)and(n % 3 == 0):
        print("Fizz Buzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else: print(n)