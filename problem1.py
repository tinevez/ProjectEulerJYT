# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

from math import floor
import timeit


def summultiple(m, alpha):
    n_alpha = floor((m-1)/alpha)
    sum_alpha = alpha / 2 * (n_alpha + 1) * n_alpha
    return sum_alpha


def summultiples(m, alpha, beta):
    sum_alpha = summultiple(m, alpha)
    sum_beta = summultiple(m, beta)
    sum_both = summultiple(m, alpha * beta)
    return sum_alpha + sum_beta - sum_both


start_time = timeit.default_timer()
val = summultiples( 1000, 3, 5 )
elapsed = timeit.default_timer() - start_time

print('Sum of multiples of 3 & 5 up to 1000 is %d.' % val )
print('Computation took %f ms' % (1000*elapsed))
