# coding: utf-8
#
# ONLY READ THIS IF YOU HAVE ALREADY SOLVED THIS PROBLEM!
# File created for http://projecteuler.net/
#
# Created by: Alex Dias Teixeira
# Name:       003_prime.py
# Date:       13 Sept 2013
#
# Problem:    [3] - Largest prime factor
#   The prime factors of 13195 are 5, 7, 13 and 29.
#
#   What is the largest prime factor of the number 600851475143?
#

def find_factors(num):
  '''
  (integer) -> integer

  This function wil calculate all the (prime)factors for num.

  >>> max(find_factors(600851475143))
  6857
  >>> max(find_factors(24))
  4
  '''

  factor = []
  prime = 2

  while prime <= num:
    if num % prime == 0:
      # Adds the factor to the list
      factor.append(prime)
      num = num / prime
      prime += 1
    else:
      prime += 1
  return factor
print max(find_factors(600851475143))
