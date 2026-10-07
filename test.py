from matplotlib import pyplot as plt
import numpy as np

t = np.linspace(0,10,10)
y = np.sin(t)
print(y)

plt.scatter(t,y)
plt.show()