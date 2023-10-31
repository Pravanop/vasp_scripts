import numpy as np
import matplotlib.pyplot as plt

# Define parameters
L = 1.0  # Length of the rod
T = 1.0  # Total time
Nx = 5  # Number of spatial grid points
Nt = 3  # Number of time steps
alpha = 1  # Thermal diffusivity

# Discretization
dx = L / Nx
dt = T / Nt
r = alpha * dt / (dx ** 2)

# Initial condition
x = np.linspace(0, L, Nx+1)
u0 = np.sin(np.pi*x)

# Initialize arrays for solution
u = np.copy(u0)
u_new = np.zeros(Nx + 1)

# Time-stepping loop (Crank-Nicolson method)
for n in range(1 , Nt + 1) :
	for i in range(1 , Nx) :
		u_new[i] = u[i] + 0.5 * r * (u[i + 1] - 2 * u[i] + u[i - 1]) + 0.5 * r * (u[i + 1] - 2 * u[i] + u[i - 1])
	
	u_new[0] = 0  # Boundary condition at x=0
	u_new[Nx] = 0  # Boundary condition at x=L
	
	u , u_new = u_new , u  # Swap u and u_new for the next time step

# Plot the solution
x = np.linspace(0 , L , Nx + 1)
plt.plot(x , u)
plt.title('Crank-Nicolson Heat Diffusion')
plt.xlabel('Position (x)')
plt.ylabel('Temperature (u)')
plt.show()