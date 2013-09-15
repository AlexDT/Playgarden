# coding: utf-8
#
# ONLY READ THIS IF YOU HAVE ALREADY SOLVED THIS PROBLEM!
# File created for http://projecteuler.net/
#
# Created by: Alex Dias Teixeira
# Name:       005_multiples.py
# Date:
#
# Problem:    [5] - Smallest multiple
#   2520 is the smallest number that can be divided by each of the numbers
#   from 1 to 10 without any remainder.
#
#   What is the smallest positive number that is evenly divisible by all
#   of the numbers from 1 to 20?
#

# def find_factors(num):
#   '''
#     (integer) -> integer

#     This function wil calculate all the (prime)factors for num.

#     >>> max(find_factors(600851475143))
#     6857
#     >>> max(find_factors(24))
#     4
#   '''

#   factor = []
#   prime = 2

#   while prime <= num:
#     if num % prime == 0:
#       # Adds the factor to the list
#       factor.append(prime)
#       num = num / prime
#       prime += 1
#     else:
#       prime += 1
#   return factor

# http://www.helpwithfractions.com/math-homework-helper/least-common-multiple/
def find_number():
  for i in range(0, 10000, 20):
    tup = ()
    for j in range(20, 0, -1):
      if i % j != 0:
        if j == 1:
          print i

print find_number()
