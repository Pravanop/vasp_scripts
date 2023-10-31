import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

x = np.linspace(0, 1, 2000)
temperature = np.linspace(100, 1000, 5000)
hmix = x*(1-x)*(4850*x + 12300*(1-x))
smix = -8.314*(x*np.log(x)+(1-x)*np.log(1-x))
gmix = [hmix - t*smix for t in temperature]

phase_boundary = []
spinodal_boundary = []
for idx, i in enumerate(gmix):
	second_derivative = np.gradient(np.gradient(i))
	inflection_points , _ = find_peaks(-second_derivative)
	temp = np.round(x[np.where(np.diff(np.sign(np.diff(i,2))))], 3)
	if len(temp) > 2:
		phase_boundary.append([temp[0], temp[-1]])
		spinodal_boundary.append([temp[1], temp[2]])
	else:
		print(temperature[idx])
		continue

plt.plot(spinodal_boundary, temperature[:len(spinodal_boundary)], marker = '.', color = 'red')
plt.xlim(0, 1)
plt.ylim(100, 800)
plt.ylabel('Temperature')
plt.xlabel('$X_{1}$')
plt.show()
# for i in gmix:
# 	plt.plot(x, i)
#
# plt.xlabel('$X_{1}$')
# plt.ylabel('$G_{mix}$')
# plt.axhline(y= 0 , c = 'black', linewidth = 0.8, alpha = 0.9)
# plt.xlim(0,1)
# plt.legend(temperature)
#
# plt.show()
#
# plt.plot(x, hmix)
# plt.xlim(0, 1)
# plt.ylim(0, 2500)
# plt.ylabel('$H_{mix}$')
# plt.xlabel('$X_{1}$')
# plt.show()