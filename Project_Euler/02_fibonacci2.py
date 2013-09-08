def fibonacci():

    a = 0
    b = 1
    c = 0
    som = 0

    while som < 4000000:
        c = a + b
        a = b
        b = c
        if c % 2 == 0:
            som = som + c
    return som


print fibonacci()
