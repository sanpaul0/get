import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap
import matplotlib.ticker as ticker

with open ('settings.txt') as set:
    settings = [float(i) for i in set.read().split('\n')]
print(settings)
fig = plt.figure(figsize = (16,9))
ax = fig.add_subplot(111)
v = np.loadtxt('data.txt', dtype = float)
u = np.arange(0, len(v), 1)
u = u/settings[0]
tz = round(u[v.argmax()], 2)
tr = round(u[-1], 2)
ax.axis([0, u.max()+1, 0, v.max() + 0.2])

ax.set_title("\n".join(wrap('Процес зарядки и разрядки конденсатора в RC-цепи',60)), loc = 'center')
ax.grid(which = 'major', color = 'k')
ax.minorticks_on()
ax.grid(which = 'minor', color = 'gray', linestyle = ':', alpha=0.5, linewidth = 0.5)
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(6))
ax.set_ylabel("U, В")
ax.set_xlabel("t, с")
ax.plot(u,v, c = 'black', linewidth=1, label="U(t)")
ax.scatter(u[0:v.size:20], v[0:v.size:20], marker = 's', c = 'blue', s = 10)
ax.legend(shadow = False, fontsize = 15)
ax.text(7, 1.75, f"Время зарядки t = :{tz}c")
ax.text(7, 1.25, f"Время разрядки t = :{round(tr - tz,2)}c")
fig.savefig('graph.svg')
plt.show()
