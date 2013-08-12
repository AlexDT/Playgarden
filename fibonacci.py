fibnumb = raw_input("Welk getal in de fibonaccireeks wil je zien?\n\n")

print "\n" + str(fibnumb), "it is!\n"


def fibonacci(fibnumb):
    a = 0
    b = 0
    c = 0
    for i in range(0, int(fibnumb)):
        if b == 0:
            b = 1
#            print str(i + 1) + ":", str(b)
        else:
            c = a + b
            a = b
            b = c
#            print str(i + 1) + ":", str(c)
    return c

number1 = fibonacci(fibnumb)
number2 = fibonacci(int(fibnumb)+1)
fib = float(number2)/number1

# print "Nummer %s in deze reeks is %s" % (str(fibnumb), number)
print "Fibonacci =", fib
