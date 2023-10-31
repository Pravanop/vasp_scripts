import numpy as np
import matplotlib.pyplot as plt
from math import factorial
from scipy.signal import find_peaks
from scipy import interpolate
def smoothListGaussian(list,degree=100):
    list =[list[0]]*(degree-1) + list + [list[-1]]*degree
    window=degree*2-1
    weight=np.array([1.0]*window)
    weightGauss=[]
    for i in range(window):
        i=i-degree+1
        frac=i/float(window)
        gauss=1/(np.exp((4*(frac))**2))
        weightGauss.append(gauss)
    weight=np.array(weightGauss)*weight
    smoothed=[0.0]*(len(list)-window)
    for i in range(len(smoothed)):
        smoothed[i]=sum(np.array(list[i:i+window])*weight)/sum(weight)
    return smoothed

x = np.linspace(0, 1, 20001)

temperature = np.linspace(100, 800, 10001)

gmix = []
for i in temperature:
	gmix.append(10600*(1-x)*x + 8.314*i*((1-x)*np.log(1-x) + x*np.log(x)))

phase_boundary = []
spinodal_boundary = []
for idx, i in enumerate(gmix):
	peaks, _ = find_peaks(-i, height = 0)
	temp = np.round(x[np.where(np.diff(np.sign(np.diff(i,2)),1))], 3)

	if len(peaks) == 0:
		phase_boundary.append([0, 1])
	
	if len(peaks) == 1:
		continue
	if len(peaks) >= 2:
		phase_boundary.append(np.round(x[peaks],3))
	
	if len(temp) > 2:
		spinodal_boundary.append([temp[1], temp[2]])
	else:
		continue

original = smoothListGaussian(list(temperature[:len(phase_boundary)]))
original_spine = smoothListGaussian(list(temperature[:len(spinodal_boundary)]))

plt.plot(spinodal_boundary, original_spine, color = 'red', linewidth = 2, linestyle = '--')
plt.plot(phase_boundary, original, color = 'blue', linewidth = 2)
plt.xlim(0, 1)
plt.ylim(100, 800)
plt.ylabel('Temperature (K)')
plt.xlabel('$X_{2}$')
# plt.legend(['Spinodal Boundary', 'Phase Boundary'])
plt.show()
