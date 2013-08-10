fibnumb = raw_input("Welk getal in de fibonaccireeks wil je zien?\n\n")

print "\n" + str(fibnumb) + " it is!\n"


def fibonacci(fibnumb):
    a = 0
    b = 0
    c = 0
    for i in range(0, int(fibnumb)):
        if b == 0:
            b = 1
        else:
            a = b
            b = c
        c = a + b
    return c

number = fibonacci(fibnumb)

print "Nummer %s in deze reeks is %s" % (str(fibnumb), number)
