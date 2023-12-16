import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 10, 0.05)
y_exact = (
    np.exp(-3*time/2)*(1 + 3*time/2 - 5*(time**2))
    )
plt.plot(time, y_exact, label='Exact')


dt = 0.05
time = np.arange(0, 10.001, dt)

f = lambda t,z1,z2: -10*np.exp(-1.5*t) - 3*z2 - 2.25*z1

z1 = np.zeros_like(time)
z2 = np.zeros_like(time)
# initial conditions
z1[0] = 1
z2[0] = 0

# Forward Euler iterations
for idx, t in enumerate(time[:-1]):
    z1[idx+1] = z1[idx] + dt*z2[idx]
    z2[idx+1] = z2[idx] + dt*f(t, z1[idx], z2[idx])

def search(time_s):
	return z1[np.where(time == time_s)], y_exact[np.where(time == time_s)], z1[np.where(time == time_s)] - y_exact[np.where(time == time_s)]

print(search(0.1))
print(search(1.6))
print(search(2.1))
print(search(4))
print(search(7))
plt.plot(time, z1, '.--', label='Forward Euler solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
# plt.show()