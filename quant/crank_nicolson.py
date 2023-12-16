import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameters
L = 1.0  # Length of the rod
T = 0.6  # Total time
dx = 0.2  # Spatial step size
dt = 0.2  # Time step size
Nx = int(L / dx)  # Number of spatial grid points
Nt = int(T / dt)  # Number of time steps
alpha = 1.0  # Thermal diffusivity

# Initialize arrays for solution
x = np.linspace(0 , L , Nx + 1)
t = np.linspace(0 , T , Nt + 1)
u = np.zeros((Nt + 1 , Nx + 1))
u[0 , :] = np.sin(np.pi * x)  # Initial condition

# Time-stepping loop (Crank-Nicolson method)
r = alpha * dt / (2 * dx ** 2)
for n in range(1 , Nt + 1) :
	A = np.zeros((Nx - 1 , Nx - 1))
	B = np.zeros(Nx - 1)
	
	for i in range(1 , Nx) :
		A[i - 1 , i - 1] = 1 + 2 * r
		if i < Nx - 1 :
			A[i - 1 , i] = -r
		if i > 1 :
			A[i - 1 , i - 2] = -r
		
		B[i - 1] = (1 - 2 * r) * u[n - 1 , i] + r * (u[n - 1 , i + 1] + u[n - 1 , i - 1])
	
	B[0] += r * 0  # Boundary condition at x=0
	u[n , 1 :Nx] = np.linalg.solve(A , B)
	u[n , 0] = u[n , 1]  # Insulated boundary condition at x=0
	u[n , Nx] = u[n , Nx - 1]  # Insulated boundary condition at x=1

# Create a 3D plot
X , T = np.meshgrid(x , t)
fig = plt.figure(figsize = (10 , 8))
ax = fig.add_subplot(111 , projection = '3d')
ax.plot_surface(X , T , u , cmap = 'plasma')
ax.set_xlabel('Position (x)')
ax.set_ylabel('Time (t)')
ax.set_zlabel('Temperature (u)')
ax.set_title('3D Plot of Temperature Evolution')
plt.show()
