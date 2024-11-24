import sympy as sp

def newton_raphson(equations, initial_guesses, tolerance=1e-7, max_iterations=100):
    """
    Encuentra la raíz de un sistema de ecuaciones usando el método de Newton-Raphson.

    Args:
        equations: Lista de ecuaciones en términos de x e y.
        initial_guesses: Lista de conjeturas iniciales para x e y.
        tolerance: Tolerancia para la convergencia.
        max_iterations: Número máximo de iteraciones.

    Returns:
        Tupla con la raíz encontrada (si convergió) y la lista de iteraciones.
    """

    x, y = sp.symbols('x y')
    f = [sp.sympify(eq) for eq in equations]

    # Derivadas parciales
    f_prime_x = [sp.diff(eq, x) for eq in f]
    f_prime_y = [sp.diff(eq, y) for eq in f]

    current_guesses = list(initial_guesses)
    iterations = []

    for i in range(max_iterations):
        # Evaluar las funciones y sus derivadas en la conjetura actual
        f_values = [eq.subs({x: current_guesses[0], y: current_guesses[1]}) for eq in f]
        f_prime_x_values = [eq.subs({x: current_guesses[0], y: current_guesses[1]}) for eq in f_prime_x]
        f_prime_y_values = [eq.subs({x: current_guesses[0], y: current_guesses[1]}) for eq in f_prime_y]

        # Verificar si alguna derivada es cero
        if any(d == 0 for d in f_prime_x_values + f_prime_y_values):
            print(f"La derivada es cero en x = {current_guesses[0]}, y = {current_guesses[1]}. No se puede continuar.")
            return None, iterations

        # Actualizar las conjeturas usando la fórmula de Newton-Raphson
        next_guesses = [
            current_guesses[0] - f_values[0] / f_prime_x_values[0],
            current_guesses[1] - f_values[1] / f_prime_y_values[1]
        ]

        iterations.append((i + 1, *current_guesses, *next_guesses, f_values[0], f_values[1]))

        # Verificar la convergencia
        if abs(next_guesses[0] - current_guesses[0]) < tolerance and abs(next_guesses[1] - current_guesses[1]) < tolerance:
            return next_guesses, iterations

        current_guesses = next_guesses

    print("No se encontró una raíz en el número máximo de iteraciones.")
    return None, iterations

def main():
    n = int(input("Ingrese la cantidad de ecuaciones a evaluar: "))
    equations = []
    initial_guesses = []

    for i in range(n):
        equation = input(f"Ingrese la ecuación {i + 1} (en términos de x e y, usando ^ para potencias, por ejemplo, 4*x^2 - y^3 + 28 = 0): ")
        # Reemplazar ^ por ** para que sea compatible con sympy
        equation = equation.replace('^', '**')
        equations.append(equation)

        initial_guess_x = float(input(f"Ingrese la conjetura inicial para x para la ecuación {i + 1}: "))
        initial_guess_y = float(input(f"Ingrese la conjetura inicial para y para la ecuación {i + 1}: "))
        initial_guesses.append((initial_guess_x, initial_guess_y))

    root, iterations = newton_raphson(equations, initial_guesses)

    if root is not None:
        print(f"\nRaíz encontrada: x = {root[0]}, y = {root[1]}")
        print("Iteraciones:")
        print("Iteración | x actual | y actual | x siguiente | y siguiente | Valor de la función 1 | Valor de la función 2")
        for iteration in iterations:
            print(f"{iteration[0]:<10} | {iteration[1]:<9} | {iteration[2]:<9} | {iteration[3]:<12} | {iteration[4]:<12} | {iteration[5]:<20} | {iteration[6]:<20}")
    else:
        print(f"No se encontró raíz.")

if __name__ == "__main__":
    main()
