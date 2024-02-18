#beautiful code btw: (sadly doesn't produce good graph)
#from sympy import plot_implicit, Eq
#from sympy.abc import x, y

# a = -4
# b = 2
# plot_implicit(Eq(y-a*x-b/x,0), (x, -10, 10), (y, -10, 10))

import numpy as np
import matplotlib.pyplot as plt
#loads values of positive and negative y
y_p=np.loadtxt("values.dat", delimiter=' ', max_rows=1)
y_n=np.loadtxt("values.dat", delimiter=' ', max_rows=1, skiprows=1)

#generate x values
x_p= np.linspace(0.01, 5, 100)  
x_n = np.linspace(-5, -0.01, 100)

#plot the graph
plt.plot(x_p, y_p, color='blue', label='$y = -4x - \\dfrac{2}{x}$')
plt.plot(x_n, y_n, color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y(x)$')
plt.grid(True)
plt.legend()
plt.savefig("../figs/fig.png")