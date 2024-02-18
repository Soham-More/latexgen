import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt('yt_data.txt')
t_values = data[:, 0]
y_values = data[:, 1]

# Plot the graph
plt.plot(t_values, y_values, label=r'$\frac{e^{-t/8}}{4\sqrt{15}} \left(9\sin\left(\frac{\sqrt{15}t}{8}\right) - \sqrt{15}\cos\left(\frac{\sqrt{15}t}{8}\right)\right)$')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.savefig('b.png')


