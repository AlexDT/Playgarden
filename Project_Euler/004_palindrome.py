#    coding: utf-8
#
#    ONLY READ THIS IF YOU HAVE ALREADY SOLVED THIS PROBLEM!
#    File created for http://projecteuler.net/
#
#    Created by: Alex Dias Teixeira
#    Name:       004_palindrome.py
#    Date:       13 Sept 2013
#
#    Problem:    [3] - Largest prime factor
#        A palindromic number reads the same both ways. The largest palindrome
#        made from the product of two 2-digit numbers is 9009 = 91 × 99.
#       
#        Find the largest palindrome made from the product of two 3-digit numbers.
#
import time

def find_palindrome():
  # (None) -> integer
  #
  # This function wil find the largest palindrome number that is the product of
  # two 3-digit numbers.
  #
  # >>> find_palindrome()
  # Time taken: 0.397763967514 sec
  # 906609

  time_start = time.time()
  pal_num = 0

  for a in range(100, 999):
    for b in range(100, 999):
      num = str(a * b)
      if num == num[::-1] and int(num) > pal_num:
        pal_num = int(num)

  time_taken = time.time() - time_start
  print "Time taken:", time_taken, "sec"
  return pal_num

#pal_num = 0
#for a in range(100, 999):
#  for b in range(100, 999):
#    num = str(a * b)
#      if num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3] and int(num) > pal_num:
#        pal_num = int(num)

#pal_num = 0
#for a in range(100, 999):
#  for b in range(100, 999):
#      num = str(a * b)
#      if num[0] == num[-1]:
#        if num[1] == num[-2]:
#          if num[2] == num[-3]:
#            if int(num) > pal_num:
#              pal_num = int(num)

print find_palindrome()


