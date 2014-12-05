# coding: utf-8
#
# ONLY READ THIS IF YOU HAVE ALREADY SOLVED THIS PROBLEM!
# File created for http://projecteuler.net/
#
# Created by: Alex Dias Teixeira
# Name:       004_palindrome.py
# Date:       13 Sept 2013
#
# Problem:    [4] - Largest palindrome product
#   A palindromic number reads the same both ways. The largest palindrome
#   made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#   Find the largest palindrome made from the product of two 3-digit
#   numbers.
#

import time

def find_palindrome():
  ''' (None) -> integer

  This function wil find the largest palindrome number that is the product of
  two 3-digit numbers.

  >>> find_palindrome()
  Time taken: 0.397763967514 sec
  906609
  '''

  time_start = time.time()
  # largest palindrome number gets stored in pal_num
  pal_num = 0

  for a in range(10, 99):
    for b in range(10, 99):
      # Turns product of a * b into a string, so it is subscriptable
      num = str(a * b)
      # Checks if the product is identical to its reversed version &
      # if the product is bigger than the previous pal_num
      if num == num[::-1] and int(num) > pal_num:
        pal_num = int(num)

  time_taken = time.time() - time_start
  print "Time taken:", time_taken, "sec"
  return pal_num

print find_palindrome()