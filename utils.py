import random

def show_random_solutions(solutions):
    print(f"Mostrando soluciones aleatorias (total: {len(solutions)}). Presiona Enter para mostrar la siguiente, o Ctrl+C para salir.\n")
    try:
        while True:
            solution = random.choice(solutions)  # Seleccionar una solución aleatoria
            print("\n".join(" ".join("Q" if cell else "." for cell in row) for row in solution))
            print("\n---\n")
            input("Presiona Enter para ver otra solución...")
    except KeyboardInterrupt:
        print("\nMostrando soluciones finalizado.")
