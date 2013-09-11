#
#    ONLY READ THIS IF YOU HAVE ALREADY SOLVED THIS PROBLEM!
#    File created for http://projecteuler.net/
#
#    Created by: Alex Dias Teixeira
#    Name:       003_prime.py
#    Date:       
#
#    Problem:    [3] - Largest prime factor
#        The prime factors of 13195 are 5, 7, 13 and 29.
#        
#        What is the largest prime factor of the number 600851475143 ?
#

num = 600851475143
factor = 2
sieve = []
sieve_neg = []

def find_prim():
    for i in range(200):
        if i % 3 != 0:
            sieve.append(i + 1)
        else:
            sieve.append(i + 1)
            sieve_neg.append(i)

#     for i in sieve:
#         print i
#         if i % 2 == 0:
#             sieve.remove(4)
#         return sieve
#     return sieve

print find_prim()