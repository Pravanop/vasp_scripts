import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 5, 10, 15, 20, 25, 30])
p = np.array([0.05, 0.12, 0.21, 0.26, 0.19, 0.14, 0.03])

print((sum(((x - sum(x*p))**2)*p))**0.5)
# plt.plot(x, p, marker = 'o')
# plt.xlabel('x')
# plt.ylabel('p(x)')
#
# plt.show()