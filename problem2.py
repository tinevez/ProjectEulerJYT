__author__ = 'Jean-Yves'
# Even Fibonacci numbers
# Problem 2
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
# even-valued terms.

# We use the fact that even numbers in the sequence appear exactly every 3 terms. Plus, a recurrence relation can be
# established for the sequence of even numbers:
#
# s(n) = 4 * s(n) + s(n-1)
# with s(0) = 0 and s(1) = 2.
#
# Here is a non-recursive solution that stores every even number up to the max.

import timeit


def sum_fibonacci_even_number(upto):
    numbers = [0]
    v = 2;
    while v < upto:
        numbers.append(v)
        v = 4 * numbers[-1] + numbers[-2]
    return sum(numbers)


start_time = timeit.default_timer()
val = sum_fibonacci_even_number( 4e6 )
elapsed = timeit.default_timer() - start_time

print('Sum of Fibonacci even numbers up to 4 millions is %d.' % val )
print('Computation took %f ms' % (1000*elapsed))
