#    coding: utf-8
#
#    ONLY READ THIS IF YOU HAVE ALREADY SOLVED THIS PROBLEM!
#    File created for http://projecteuler.net/
#
#    Created by: Alex Dias Teixeira
#    Name:       001_sum.py
#    Date:       06 Sept 2013
#
#    Problem:    [1] - Multiples of 3 and 5
#        If we list all the natural numbers below 10 that are multiples of 3 or 5,
#        we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#        Find the sum of all the multiples of 3 or 5 below 1000.
#

total = 0
# Loops tru every numbr till 1000
for i in range(1000):
  # Checks if i can be divided by 3 or 5
  if (i % 3 == 0) or (i % 5 == 0):
    # Adds a qualifying number to the total
    total = total + i

print total
