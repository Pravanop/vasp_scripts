import numpy as np
from scipy.interpolate import interp1d

def light_intensity(x):
	return (x)/((x**2 + 325)**1.5)

def light_intensity_diff(x):
	return (1/((x**2 + 325)**1.5)) - ((3*x**2)/((x**2 + 325)**2.5))

t = 5
e = 1e-5
x1 = 0.1
f1 = light_intensity(x1)
fp1 = light_intensity_diff(x1)

a, b, c, d = 0, 0, 0, 0
for count in range(100000):
	ft = light_intensity(t)
	fpt = light_intensity_diff(t)
	
	if ft > f1 or fpt > 0:
		x2 = t
		f2 = ft
		fp2 = fpt
		A = [[1, x1, x1**2, x1**3], [0, 1, 2*x1, 3*x1**2],[1, x2, x2**2, x2**3], [0, 1, 2*x2, 3*x2**2]]
		B = [f1, fp1, f2, fp2]
		coeff = np.linalg.solve(A, B)
		print(coeff)
		xs = (4*(coeff[2]**2) - 12*coeff[1])
		xs = (-2 + xs)/(6*coeff[3])
		if abs(light_intensity_diff(xs)) <= e:
			print(xs, light_intensity(xs), count)
			break
		else:
			if light_intensity_diff(xs) < 0:
				x1 = xs
				f1 = light_intensity(x1)
				fp1 = light_intensity_diff(x1)
				continue
			else:
				t = xs
				ft = light_intensity(x1)
				fpt = light_intensity_diff(x1)
				continue
				
	else:
		x1 = t
		t = 2*t
		ft = light_intensity(t)
		fpt = light_intensity_diff(t)
		continue
	
