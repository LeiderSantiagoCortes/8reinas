import simpy
from simulation import NQueensSimulation
from plot_elapsed_times import plot_elapsed_times

SIMULATION_TIME = 8 * 60 * 60  # 8 hours


def main() -> None:
    """Main function to set up and run the simulation."""
    print("Simulation Started.")
    env = simpy.Environment()
    simulation = NQueensSimulation(env)

    # Start the process to generate robots
    env.process(simulation.generate_robots())

    # Run the simulation for the specified duration
    env.run(until=SIMULATION_TIME)

    # Print the total profit after simulation completion
    print(f"Simulation completed. Total profit: {simulation.profit}")

    # Plot the elapsed times
    plot_elapsed_times(simulation.elapsed_times, simulation.sizes)


if __name__ == "__main__":
    main()
