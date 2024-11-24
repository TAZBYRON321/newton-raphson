import sympy as sp

def newton_raphson(equation, initial_guess_x, initial_guess_y, tolerance=1e-7, max_iterations=100):
    x, y = sp.symbols('x y')
    f = sp.sympify(equation)
    
    # Derivadas parciales
    f_prime_x = sp.diff(f, x)
    f_prime_y = sp.diff(f, y)
    
    current_guess_x = initial_guess_x
    current_guess_y = initial_guess_y
    iterations = []

    for i in range(max_iterations):
        current_value = f.subs({x: current_guess_x, y: current_guess_y})
        current_derivative_x = f_prime_x.subs({x: current_guess_x, y: current_guess_y})
        current_derivative_y = f_prime_y.subs({x: current_guess_x, y: current_guess_y})
        
        if current_derivative_x == 0 or current_derivative_y == 0:
            print(f"La derivada es cero en x = {current_guess_x}, y = {current_guess_y}. No se puede continuar.")
            return None, iterations
        
        # Actualización de las conjeturas
        next_guess_x = current_guess_x - current_value / current_derivative_x
        next_guess_y = current_guess_y - current_value / current_derivative_y
        
        iterations.append((i + 1, current_guess_x, current_guess_y, next_guess_x, next_guess_y, current_value))
        
        if abs(next_guess_x - current_guess_x) < tolerance and abs(next_guess_y - current_guess_y) < tolerance:
            return (next_guess_x, next_guess_y), iterations
        
        current_guess_x = next_guess_x
        current_guess_y = next_guess_y
    
    print("No se encontró una raíz en el número máximo de iteraciones.")
    return None, iterations

def main():
    n = int(input("Ingrese la cantidad de ecuaciones a evaluar: "))
    results = []

    for i in range(n):
        equation = input(f"Ingrese la ecuación {i + 1} (en términos de x e y, usando ^ para potencias, por ejemplo, 4*x^2 - y^3 + 28 = 0): ")
        # Reemplazar ^ por ** para que sea compatible con sympy
        equation = equation.replace('^', '**')
        
        initial_guess_x = float(input(f"Ingrese la conjetura inicial para x para la ecuación {i + 1}: "))
        initial_guess_y = float(input(f"Ingrese la conjetura inicial para y para la ecuación {i + 1}: "))
        
        root, iterations = newton_raphson(equation, initial_guess_x, initial_guess_y)
        
        if root is not None:
            print(f"\nRaíz encontrada para la ecuación {i + 1}: x = {root[0]}, y = {root[1]}")
            print("Iteraciones:")
            print("Iteración | x actual | y actual | x siguiente | y siguiente | Valor de la función")
            for iteration in iterations:
                print(f"{iteration[0]:<10} | {iteration[1]:<9} | {iteration[2]:<9} | {iteration[3]:<12} | {iteration[4]:<12} | {iteration[5]:<20}")
        else:
            print(f"No se encontró raíz para la ecuación {i + 1}.")

if __name__ == "__main__":
    main()