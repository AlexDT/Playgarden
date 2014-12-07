# coding: utf-8
#
# ONLY READ THIS IF YOU HAVE ALREADY SOLVED THIS PROBLEM!
# File created for http://projecteuler.net/
#
# Created by: Alex Dias Teixeira
# Name:       016_power_sum.py
# Date:
#
# Problem:    [16] - Power digit sum
#   2**(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#   What is the sum of the digits of the number 2**(1000)?
#

exp = 1000
num = 2**exp
sum_num = 0

for i in str(num):
  sum_num += int(i)

print sum_num