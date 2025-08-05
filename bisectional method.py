import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 - x - 4

def bisection(f, a, b, tol=1e-4):
    midpoints = []
    if f(a) * f(b) > 0:
        print("f(a) and f(b) must have opposite signs")
        return None

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        midpoints.append(c)
        if f(c) == 0 or (b - a) / 2 < tol:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c, midpoints

root, steps = bisection(f, 2, 3)

if root is not None:
    print(f"Root ≈ {root}")
    print(f"Iterations: {len(steps)}")

    plt.plot(steps, 'o-')
    plt.title("Bisection Method Convergence")
    plt.xlabel("Iteration")
    plt.ylabel("Midpoint (c)")
    plt.grid(True)
    plt.show()
