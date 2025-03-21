from itertools import permutations, combinations, product, combinations_with_replacement
import scipy
import scipy.stats
import numpy as np

print(list(permutations([1, 2, 3], 2)))
print(list(combinations([1, 2, 3], 2)))
print(list(product([1, 2, 3], repeat= 2)))
print(list(product('abc' , range(3))))
print(list(combinations_with_replacement('abcd', 2)))

x = np.arange(10)
stat = scipy.stats.binom(10, 0.5)
print(stat.pmf(x))
print(stat.cdf(x))
np.random.binomial(10, 1, 10)
