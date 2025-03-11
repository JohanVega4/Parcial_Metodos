import sympy as sp

# Función generica (ejemplo: x^3 - 2x - 5)
def funcion(x):
    return x**3 - 2*x - 5

# Derivada de la función
def derivada(func):
    x = sp.symbols('x')
    expr = func(x)
    deriv = sp.diff(expr, x)
    return sp.lambdify(x, deriv, "numpy")

# Implementación de Newton-Raphson
def newton_raphson(func, tolerancia=0.001, max_iter=10, x0=1.0):
    f = sp.lambdify('x', func, 'numpy')
    f_prime = derivada(func)

    x_n = x0
    for i in range(max_iter):
        f_xn = f(x_n)
        f_prime_xn = f_prime(x_n)

        if abs(f_xn) < tolerancia:
            print(f"Raíz encontrada: {x_n} en {i+1} iteraciones")
            return x_n

        if f_prime_xn == 0:
            print("Derivada cero, no se puede continuar.")
            return None

        # Método de Newton-Raphson
        x_n = x_n - f_xn / f_prime_xn

    print("Se alcanzó el número máximo de iteraciones.")
    return x_n

# Ejemplo de uso
raiz = newton_raphson(funcion, tolerancia=0.001, max_iter=10, x0=2.0)