// coding: utf-8
//
// ONLY READ THIS IF YOU HAVE ALREADY SOLVED THIS PROBLEM!
// File created for http://projecteuler.net/
//
// Created by: Alex Dias Teixeira
// Name:       001_sum.py
// Date:       06 Sept 2013
//
// Problem:    [1] - Multiples of 3 and 5
//   If we list all the natural numbers below 10 that are multiples of
//   3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
//   Find the sum of all the multiples of 3 or 5 below 1000.
//

import UIKit

func sum_even_fib_numbers(x: Int) -> Int {
    /*
    (None) -> integer

    This function will generate an integer. This integer is the sum of all the
    even fibonacci number under 4.000.000.

    Maximum fibonacci number to add to the total? [integer]
    4000000
    4613732
    Maximum fibonacci number to add to the total? [integer]
    5
    10
    */
    
    var a = 0
    var b = 1
    var c = 0
    
    var total = 0
    
    while total < x {
        c = a + b
        a = b
        b = c
        
        if c % 2 == 0 {
            total = total + c
        }
    }
    return total
}

println(sum_even_fib_numbers(4000000))