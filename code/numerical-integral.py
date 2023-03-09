import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*x

delta_x = 0.1
x = np.arange(-10,10,delta_x)
fx = f(x)*delta_x
y = fx.cumsum()

plt.plot(x,y)
plt.show()