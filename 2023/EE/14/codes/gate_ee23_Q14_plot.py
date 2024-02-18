import numpy as np
import matplotlib.pyplot as plt

# Load data from the text file
data = np.loadtxt("data.txt", skiprows=1)

#clear all the previous outputs
plt.close("all")

# Extract columns
time = data[:, 0]
y1 = data[:, 1]
y2 = data[:, 2]

# Plot the graph for y(t)
plt.plot(time, y1, label=r'$u(t) + 2t e^{-t}u(t) - e^{-t}u(t)$', linestyle='-', color='blue', linewidth=2)
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.axhline(y=1, color='green', linestyle='--', label='y(t) Convergence at +1')
plt.legend()
plt.title('Graph of y(t)')
plt.grid(True)
plt.savefig("Plot of y(t)")
plt.clf()

# Plot the graph for w(t)
plt.plot(time, y2, label=r'$4e^{-t}u(t) - u(t) -4t e^{-t}u(t)$', linestyle='-', color='red', linewidth=2)
plt.xlabel('Time')
plt.ylabel('w(t)')
plt.axhline(y=-1, color='brown', linestyle='--', label='w(t) Convergence at -1')
plt.legend()
plt.title('Graph of w(t)')
plt.grid(True)
plt.savefig("Plot of w(t)")
plt.clf()
