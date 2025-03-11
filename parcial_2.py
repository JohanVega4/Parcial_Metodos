import sympy as sp

def newton_raphson(func_str, x0, tol=1e-6, max_iter=100):
    """
    Método de Newton-Raphson para encontrar raíces de una función
    
    Parámetros:
    func_str (str): Función en términos de 'x' (ej. 'x**3 - 2*x - 5')
    x0 (float): Valor inicial
    tol (float): Tolerancia para convergencia
    max_iter (int): Número máximo de iteraciones
    
    Retorna:
    float: Aproximación de la raíz
    """
    x = sp.symbols('x')
    try:
        f_expr = sp.sympify(func_str)
    except sp.SympifyError:
        raise ValueError("Expresión de función no válida")
    
    f = sp.lambdify(x, f_expr, 'numpy')
    f_prime = sp.lambdify(x, f_expr.diff(x), 'numpy')
    
    x_actual = x0
    for _ in range(max_iter):
        f_val = f(x_actual)
        if abs(f_val) < tol:
            return x_actual
        
        f_derivada = f_prime(x_actual)
        if abs(f_derivada) < 1e-15:
            raise ValueError("Derivada cero. No se puede continuar")
        
        x_siguiente = x_actual - f_val / f_derivada
        if abs(x_siguiente - x_actual) < tol:
            return x_siguiente
        
        x_actual = x_siguiente
    
    raise ValueError("Máximo de iteraciones alcanzado sin converger")

def secante(func_str, x0, x1, tol=1e-6, max_iter=100):
    """
    Método de la Secante para encontrar raíces de una función
    
    Parámetros:
    func_str (str): Función en términos de 'x' (ej. 'x**3 - 2*x - 5')
    x0 (float): Primer valor inicial
    x1 (float): Segundo valor inicial
    tol (float): Tolerancia para convergencia
    max_iter (int): Número máximo de iteraciones
    
    Retorna:
    float: Aproximación de la raíz
    """
    x = sp.symbols('x')
    try:
        f_expr = sp.sympify(func_str)
    except sp.SympifyError:
        raise ValueError("Expresión de función no válida")
    
    f = sp.lambdify(x, f_expr, 'numpy')
    
    a, b = x0, x1
    fa, fb = f(a), f(b)
    
    for _ in range(max_iter):
        if abs(fa) > abs(fb):
            a, b = b, a
            fa, fb = fb, fa
            
        if abs(fb) < tol:
            return b
        
        if abs(fa - fb) < 1e-15:
            raise ValueError("Diferencia entre evaluaciones cercana a cero")
        
        # Calcular nuevo punto
        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)
        
        # Verificar convergencia
        if abs(c - b) < tol:
            return c
        
        # Actualizar valores para siguiente iteración
        a, b = b, c
        fa, fb = fb, fc
    
    raise ValueError("Máximo de iteraciones alcanzado sin converger")

# Ejemplo de uso:
if __name__ == "__main__":
    # Ejemplo con Newton-Raphson
    funcion = "x**3 - 2*x - 5"
    raiz_nr = newton_raphson(funcion, x0=2.0)
    print(f"Newton-Raphson: Raíz en {raiz_nr:.6f}")
    
    # Ejemplo con Secante
    raiz_sec = secante(funcion, x0=2.0, x1=3.0)
    print(f"Método de la Secante: Raíz en {raiz_sec:.6f}")