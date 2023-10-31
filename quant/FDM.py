import numpy as np
import matplotlib.pyplot as plt


# n =8
# h = (0-1.5)/n
#
# A = np.zeros((n + 1, n + 1))
# A[0][0] = 1
# A[n, n] = 1
# for i in range(1, n):
# 	A[i, i - 1] = 9
# 	A[i, i] = (np.pi*h)**2 - 18
# 	A[i, i +1] = 9
#
#
# b = np.zeros(n+1)
# for i in range(1,n):
# 	b[i] = 0
# b[0] = -1
# b[-1] = 3
#
# y = np.linalg.solve(A,b)
#
# t = np.linspace(0,1.5 , n + 1)
# print(y)
# plt.plot(t, y, c= 'red', linewidth = 1)

n = 100
h = (0-36)/n

A = np.zeros((n + 1, n + 1))
A[0][0] = 1
A[n, n] = 1
E = 30e6
I = 1
for i in range(1, n):
	A[i, i - 2] = 1*(E*I)
	A[i, i - 1] = -4*(E*I)
	A[i, i] = 100*(h**4)  + 6*(E*I)
	A[i, i +1] =-4*(E*I)
	if i == n-1:
		continue
	else:
		A[i, i +2] = 1*(E*I)

b = np.zeros(n+1)
for i in range(1,n):
	b[i] = (h**4)*500
b[0] = 0
b[-1] = 0

y = np.linalg.solve(A,b)

t = np.linspace(0,1.5 , n + 1)
print(max(y))
plt.plot(t, y, c = 'black', alpha = 0.5, linewidth = 3)
plt.show()