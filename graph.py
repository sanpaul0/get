import matplotlib.pyplot as plt
import numpy as np



fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111)
u = np.array([255, 127, 64,32,5,0])
v = np.array([3.23, 1.66, 0.86, 0.46, 0.12, 0.05])
ax1.scatter(u,v,marker = '.')
x = np.polyfit(u,v,1)
p = np.poly1d(x)
ax1.plot(u, p(u), 'k')
ax1.grid
plt.show()