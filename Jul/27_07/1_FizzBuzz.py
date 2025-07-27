'''
FizzBuzz with a twist
Print numbers from 1 to 100. Replace:

Multiples of 3 with "Fizz"

Multiples of 5 with "Buzz"

Multiples of both with "FizzBuzz"

BUT: Add a rule to replace numbers divisible by 7 with "Bazz"
'''

for i in range(1,101):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 7 == 0:
        print("Bazz")
    else:
        print(i)

