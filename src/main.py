import simpy
from simulation import NQueensSimulation
from plot_elapsed_times import plot_elapsed_times

SIMULATION_TIME = 8 * 60 * 60  # 8 hours


def main() -> None:
    """Main function to set up and run the simulation."""
    print("Simulation Started.")
    env = simpy.Environment()
    simulation_config = {
        "uniform_distribution": [10, 30],
        "penalties": 10,
        "rewards": 15,
        "sizes": [4, 5, 6, 8, 10, 12, 15],
    }

    
  
    
    while True:
        print("Seleccione un Escenario.")
        
        print("0. Simulación por defecto")
        print("1. Modificación del Tiempo de Llegada de los Robots")
        print("2. Ajuste de Recompensas y Penalizaciones")
        print("3. Selección Sesgada de Tableros")
        
        opcion = int(input())
        
    
            
        if opcion == 1:
            simulation_config["uniform_distribution"] = [5, 15]
        elif opcion == 2:
            simulation_config["penalties"] = 20
            simulation_config["rewards"] = - 5
        elif opcion == 3:
            simulation_config["sizes"] =  [4, 5, 6]
        elif opcion != 0:
            print("Opción no válida.")
            # clear screen
            print("\033[H\033[J")
            continue
            
        simulation = NQueensSimulation(env, simulation_config)
        
        # Start the process to generate robots
        env.process(simulation.generate_robots())

        # Run the simulation for the specified duration
        env.run(until=SIMULATION_TIME)

        # Print the total profit after simulation completion
        print(f"Simulation completed. Total profit: {simulation.profit}")

        # Plot the elapsed times
        plot_elapsed_times(simulation.elapsed_times, simulation.sizes)
        break


if __name__ == "__main__":
    main()
