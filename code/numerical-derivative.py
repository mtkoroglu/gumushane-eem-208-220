import numpy as np
import matplotlib.pyplot as plt
 
# Girişin karesinin alan fonksiyonu tanımlayalım
def f(x):
    return x**2
 
# x=-10'dan x=10'a kadar örnek üretelim
x = np.linspace(-10,10,500)
y = f(x)
# grafiğin sol tarafına f(x)'i çizdirelim
fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(121)
ax.plot(x, y)
ax.set_title("y=f(x)")
 
# nümerik ve analitik türevler: f'(x) hesaplayalım
delta_x = 0.0001
y1 = (f(x+delta_x) - f(x)) / delta_x # nümerik
y2 = 2 * x # analitik
# grafiğin sağ tarafına f'(x)'i çizdirelim
ax = fig.add_subplot(122)
ax.plot(x, y1, c="r", alpha=0.5, label="numerical")
ax.plot(x, y2, c="b", alpha=0.5, label="analytical")
ax.set_title("y=f'(x)")
ax.legend()
 
plt.show()