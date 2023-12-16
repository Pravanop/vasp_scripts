from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
x = np.array([0, 10, 15, 20, 22.5, 30])
y = np.array([0, 227.04, 362.78, 517.35, 602.97, 901.67])
cs = interpolate.CubicSpline(x, y)
plt.plot(x, cs(x))
plt.scatter(x, y)
plt.xlabel('t')
plt.ylabel('v')
plt.show()