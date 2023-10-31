import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-20, 80, 101)

for i in [30, 40, 50, 60, 70, 80]:
	i = i - 32
	i = i*5/9
	i += 273.15
	x0 = x - 32
	x0 = (x0*5)/9
	x0 += 273.15
	coeff = 10.7e-3/2*i**2 - 0.33e5/i - 45.44*i
	coeff = coeff/8.314
	y = np.exp((41000/8.314)*(1/i - 1/x0))*100
	plt.plot(x,y)

plt.ylabel('Relative Humidity (%)')
plt.ylim(0, 100)
plt.xlabel('Dewpoint temperature (F)')
plt.axvline(x = 0, linestyle = '--', linewidth = 0.8, alpha = 0.8)
plt.legend(['30F', '40F', '50F', '60F', '70F', '80F'])
print(55.40* -6.44e-3*0.5*910000+7.11e-6*973000000/3)
# plt.show()