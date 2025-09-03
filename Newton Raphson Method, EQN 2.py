import math
import sys

def f(x):
    return math.sin(x) - 1 - x**3

def df(x):
    return math.cos(x) - 3*x**2

def newton_raphson_solver():
    x0 = 0.5
    tol = 0.0001
    max_iter = 100

    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)

        if abs(dfx) < 1e-12:
            print("Derivative is zero or too small. Method fails.")
            sys.exit()

        x1 = x0 - fx / dfx

        print(f"Iteration {i + 1}: x = {x1}")

        if math.fabs(x1 - x0) < tol:
            print(f"Approximate Root = {x1}")
            return

        x0 = x1

    print(f"Method did not converge after {max_iter} iterations.")

if __name__ == "__main__":
    newton_raphson_solver()

