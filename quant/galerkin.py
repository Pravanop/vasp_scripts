import numpy as np
from sympy import *
import matplotlib.pyplot as plt
sum = __builtins__.sum

def galerkin(ode, x, x0, x1, u0, q):
    basis = [x**k for k in range(q+1)]
    # Coefficients for the basis monomials
    xi = [Symbol("xi_%i" % k) for k in range(q+1)]
    # Solution function ansatz
    u = u0 + sum(xi[k]*basis[k] for k in range(1,q+1))
    # Form system of linear equations
    equations = [integrate(ode(u)*basis[k], (x, x0, x1)) \
        for k in range(1,q+1)]
    coeffs = solve(equations, xi[1:])
    return u.subs(coeffs)

x = Symbol('x')
ode = lambda u: -u.diff(x,2) + u + 8 - 16*x**2 + x**4

galerkin_solution = galerkin(ode, x, 0, 2, 0, 3)
pprint(galerkin_solution)
x = np.linspace(0,2,100)
galerkin_solution3 = -4*x**3 + 7.5*x**2 + (2-16*49/480)*x
galerkin_solution4 = -x**4 + 4*x**2
exact_solution = -(x**2) *(x**2 - 4)

plt.plot(x, galerkin_solution3)
plt.plot(x, galerkin_solution4)
plt.plot(x, exact_solution, alpha = 0.5)
plt.legend(['Galerkin solution with cubic basis', 'Galerkin solution with quartic basis', 'Exact solution' ])
plt.show()

