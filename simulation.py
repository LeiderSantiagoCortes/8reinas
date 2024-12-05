import random
import time
from solver_robot import LasVegasSolver
from solver_professor import DeterministicSolver

def run_simulation():
    sizes = [4, 5, 6, 8, 10, 12, 15]
    duration = 8 * 3600  # 8 horas en segundos
    elapsed_time = 0

    print("Iniciando simulación...\n")
    while elapsed_time < duration:
        # Seleccionar tamaño del tablero
        size = random.choice(sizes)
        print(f"Tablero seleccionado: {size}x{size}")

        # Iniciar jugadores
        robot_solver = LasVegasSolver(size)
        professor_solver = DeterministicSolver(size)

        # Tiempos de resolución
        robot_time = random.randint(10, 30)
        professor_time = size  # Tiempo proporcional al tamaño para el profesor

        # Resolver el problema
        robot_start = elapsed_time + robot_time
        professor_start = elapsed_time + professor_time

        if robot_start < professor_start:
            robot_solver.solve()
            print("El robot ha ganado.\n")
        else:
            professor_solver.solve()
            print("El profesor ha ganado.\n")

        elapsed_time += max(robot_time, professor_time)

    print("Simulación completada.")
