
# -*- coding: utf-8 -*su
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 + 3

x = np.arange(46)

plt.plot(x, f(x))
plt.show()

