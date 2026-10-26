#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 0, 1.0

best = 0.0
v = []
for i in range( 10000):
    s = np.random.normal(mu, sigma, 20)

    x = abs(mu - np.mean(s))
    if x > best:
        v = s
        best = x
s = np.random.normal(mu, sigma, 20000)
count, bins, ignored = plt.hist(s, 30)
s = np.random.normal(mu, sigma, 2000)
count, bins, ignored = plt.hist(s, 30)
s = np.random.normal(mu, sigma, 200)
count, bins, ignored = plt.hist(s, 30)
print( 'best', best)
count, bins, ignored = plt.hist(v, 30)#, density=True)
plt.semilogy()

#plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()
