import numpy as np
import matplotlib.pyplot as plt

method = ['Euler']

h = 0.01
start = 0
stop = 1
x = np.linspace(start= start, stop= stop, num= int((stop-start)/h))
def yp(x, y):
	return 2 - 3*x + 4*y

def quadratic_root_solver(a, b, c):
	return [(-b + (b**2 - 4*a*c)**0.5)/(2*a), (-b - (b**2 - 4*a*c)**0.5)/(2*a)]

def euler(x, h):
	y0 = 1
	y_num = []
	for idx, i in enumerate(x):
		if idx == 0:
			yp0 = yp(i, y0)
			y_next = y0 + h*yp0
			y_num.append(y_next)
		else:
			y_prev = y_num[idx - 1]
			y_next = y_prev + h*yp(i, y_prev)
			y_num.append(y_next)
	return [y0] + y_num[:-1]
# def range_kutta():
# 	y0 = 1
# 	y_num = []
# 	for idx , i in enumerate(x) :
# 		if idx == 0:
# 			k1 = yp(y0)
# 			k2 = yp(y0 + 0.5*h*k1)
# 			k3 = yp(y0 + 0.5*h*k2)
# 			k4 = yp(y0 + h*k3)
# 			y_next = y0 + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
# 			y_num.append(y_next)
# 		else:
# 			y_prev = y_num[idx - 1]
# 			k1 = yp(y_prev)
# 			k2 = yp(y_prev + 0.5 * h * k1)
# 			k3 = yp(y_prev + 0.5 * h * k2)
# 			k4 = yp(y_prev + h * k3)
# 			y_next = y_prev + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
# 			y_num.append(y_next)
# 	return [y0] + y_num[:-1]

# def predictor_corrector():
# 	y0 = 1
# 	y_num = []
# 	for idx , i in enumerate(x) :
# 		if idx == 0 :
# 			roots = quadratic_root_solver(h*0.5, 1, (-2*y0 +h*y0**2)/2)
# 			y_next = max(roots)
# 			y_num.append(y_next)
# 		else :
# 			y_prev = y_num[idx - 1]
# 			roots = quadratic_root_solver(h*0.5, 1, (-2*y_prev +h*y_prev**2)/2)
# 			y_next = max(roots)
# 			y_num.append(y_next)
# 	return [y0] + y_num[:-1]

methods = [euler]
for idx in range(len(methods)):
	plt.plot(x, methods[0](x,h), c = "#EE7733" , marker = 'o' , alpha = 0.8)
	h = 0.1
	x = np.linspace(start = start , stop = stop , num = int((stop - start) / h))
	plt.plot(x, methods[0](x, h), c = "#0077BB" , marker = 's' , alpha = 0.8)
	h = 0.001
	x = np.linspace(start = start , stop = stop , num = int((stop - start) / h))
	plt.plot(x, methods[0](x, h), c = "#009988" , marker = 'x' , alpha = 0.8)
	
	plt.legend(['h = 0.01', 'h = 0.1', 'h = 0.0001'])
	plt.ylabel('Y')
	plt.xlabel('X')
	plt.show()
	
