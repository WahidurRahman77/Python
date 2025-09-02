import sys

def f(x):
    return x**3 + 2*x**2 + 10*x - 20

def df(x):
    return 3*x**2 + 4*x + 10

def newton_raphson_solver():
   
    x0 = 1.0          
    tol = 0.0001    
    max_iter = 100    

    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)

        if abs(dfx) < 1e-12:
            print("Derivative is zero or too small. Cannot continue.")
            sys.exit()

        x1 = x0 - fx / dfx

        print(f"Iteration {i + 1:2d}: x = {x1:.8f}")

        if abs(x1 - x0) < tol:
            print(f"Approximate Root = {x1:.8f}")
            return

        x0 = x1

    print(f"\nMethod did not converge after {max_iter} iterations.")

if __name__ == "__main__":
    newton_raphson_solver()