import numpy as np

# Función generica (ejemplo: x^3 - 2x - 5)
def funcion(x):
    return x**3 - 2*x - 5

# Implementación del Método de la Secante
def secante(func, tolerancia=0.001, max_iter=10, x0=1.0, x1=2.0):
    for i in range(max_iter):
        f_x0 = func(x0)
        f_x1 = func(x1)

        if abs(f_x1) < tolerancia:
            print(f"Raíz encontrada: {x1} en {i+1} iteraciones")
            return x1

        # Fórmula de la secante
        denominador = f_x1 - f_x0
        if denominador == 0:
            print("Denominador cero, no se puede continuar.")
            return None

        # Actualización de los valores
        x2 = x1 - f_x1 * (x1 - x0) / denominador
        x0, x1 = x1, x2

    print("Se alcanzó el número máximo de iteraciones.")
    return x1

# Ejemplo de uso
raiz = secante(funcion, tolerancia=0.001, max_iter=10, x0=1.0, x1=2.0)