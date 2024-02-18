import matplotlib.pyplot as plt
import numpy as np

with open("values.dat") as file:
    data_str = file.read()

sequences = data_str.split('\n')
sequences = np.array(sequences)[np.where(np.array(sequences) != "")].tolist()
data_array = np.array(list(map(np.vectorize(float), map(lambda line: line.split('\t'), sequences))))

t = data_array[:, 0]  # the time axis values
x = data_array[:, 1]  # values of x(t)

plt.plot(t, x, 'b-')  # plot all points in blue

t_zero_idx = np.where(t == 0)[0][0]#when t=0
t_6_28_idx = np.where(np.isclose(t, 6.28))[0][0] #When t =6.28  
#plot two special points in red and green
plt.plot(t[t_zero_idx], x[t_zero_idx], 'ro', label='t=0')  # x(0)
plt.plot(t[t_6_28_idx], x[t_6_28_idx], 'go', label='t=6.28')  # x(6.28)

plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend(loc = 'lower right')
plt.savefig("Figure_1.png")
#plt.show()
