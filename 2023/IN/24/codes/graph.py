import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the coefficients of the polynomial
coefficients = [1, 2, 5, 80]

# Find the roots (zeros) and poles of the polynomial
zeros, poles, _ = signal.tf2zpk(coefficients, [1])
# s1 = -4.63925
# s2 = 1.31963 + 3.93735 i
# s3 = 1.31963 - 3.93735 i
# Plot the pole-zero plot
plt.figure(figsize=(8, 6))
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='b', label='Zeros')
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', label='Poles')
plt.axhline(0, color='black', linewidth=1.5)
plt.axvline(0, color='black', linewidth=1.5)

plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.legend()
plt.grid(True)
plt.savefig('poles and root_plot.png')
plt.show()
