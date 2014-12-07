number1 = int(raw_input("Vanaf welk getal wil je beginnen?"))
number2 = int(raw_input("Waar wil je eindigen?"))


def fizzBuzz(x):

    if x % 3 == 0 and x % 5 == 0:
        print str(x) + ": FizzBuzz"
    elif x % 3 == 0:
        print str(x) + ": Fizz"
    elif x % 5 == 0:
        print str(x) + ": Buzz"
    else:
        print str(x) + ": " + str(x)

for x in range(number1, number2):
    fizzBuzz(x)
