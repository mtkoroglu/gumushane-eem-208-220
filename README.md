<h1>EEM 208/220 Mühendislik Matematiği</h1>
<h2>Nümerik Türev</h2>
<p align="justify">Türev operatörü bir fonksiyonun değişimini hesaplar. Bir fonksiyonun bir noktadaki türevi o noktadaki eğimidir. Örnek olarak, eğer $f(x)=x^2$ şeklinde bir fonksiyon için, $x$ noktasındaki değişimi veren fark denklemini yazacak olursak, küçük $\delta x$ değerleri için</p>

```math
f'(x) = \frac{f(x+\delta x)-f(x)}{\delta x}
```

<p align="justify">elde edilir. Bu şekilde örnekler üzerinde fark denklemiyle hesaplanan türev nümeriktir. Aşağıda kodda hem nümerik hem analitik türevi hesaplayıp çizdirelim.</p>

```
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
```

<figure>
    <img src="figure/plot.jpg" alt="first example" width=%100 height=auto>
    <figcaption>Nümerik ve abalitik türevi alınan kare fonksiyonu</figcaption>
</figure>

<p>We can similarly do a differentiation of other functions. For example, $f(x)=x^3-2x^2+1$. Find the derivative of this function using the rules of differentiation and compare your result with the result found using the rate of limits. Verify your result with the plot above. If you’re doing it correctly, you should see the following graph:</p>


<h2>Kaynaklar</h2>
[1] https://machinelearningmastery.com/calculus-for-machine-learning-7-day-mini-course/