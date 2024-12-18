import random
import simpy
from solver_robot import LasVegasSolver
from solver_professor import DeterministicSolver
import time

# Possible board sizes for the N-Queens problem



class NQueensSimulation:
    """
    Simulates the N-Queens problem where a robot and a professor compete to solve the puzzle.
    The simulation tracks the profit based on which solver wins each game.
    """

    def __init__(self, env: simpy.Environment, simulation_config: dict):
        """
        Initialize the NQueensSimulation with the simulation environment.

        Args:
            env (simpy.Environment): The simulation environment.
        """
        self.env = env
        self.sizes = simulation_config["sizes"]
        
        self.uniform_distribution = simulation_config["uniform_distribution"]
        self.penalties = simulation_config["penalties"]
        self.rewards = simulation_config["rewards"]
        
        self.profit = 0  # Tracks the total profit from the simulation
        
        # Dictionary to store real elapsed times separately for Las Vegas and Deterministic solvers
        self.elapsed_times = {
            "LasVegas": {size: [] for size in self.sizes},
            "Deterministic": {size: [] for size in self.sizes},
        }

    def generate_robots(self):
        """
        Continuously generates robots at random intervals and starts the game process.
        """
        while True:
            # Wait for a random time between 10 and 30 seconds before generating the next robot
            timeout_duration = random.randint(self.uniform_distribution[0], self.uniform_distribution[1])
            print(
                f"Waiting for {
                    timeout_duration} seconds before generating a new robot."
            )
            yield self.env.timeout(timeout_duration)
            # Start a new game process
            print("Generating a new robot.")
            self.env.process(self.play_game())

    def play_game(self):
        """
        Simulates a single game where a robot and a professor attempt to solve the N-Queens problem.
        Determines the winner based on the time taken to solve the problem and updates the profit accordingly.
        """
        # Select a random board size for the game
        size = random.choice(self.sizes)
        print(f"Selected board size: {size}x{size}")

        # Initialize the solvers with the selected board size
        robot_solver = LasVegasSolver(size, self.uniform_distribution)
        professor_solver = DeterministicSolver(size)

        # Get the time taken by each solver to solve the problem
        robot_time = robot_solver.solve_time()
        professor_time = professor_solver.solve_time()

        print(f"Robot will take {robot_time:.2f} seconds to solve.")
        print(f"Professor will take {professor_time:.2f} seconds to solve.")

        # Measure and store the real elapsed time for the robot solver
        robot_start_time = time.time()
        yield self.env.timeout(robot_time)
        print("Robot started solving the problem.")
        robot_solved = robot_solver.solve()
        robot_elapsed_time = time.time() - robot_start_time
        self.elapsed_times["LasVegas"][size].append(robot_elapsed_time)
        print(f"Real elapsed time for Las Vegas solver on board size {
              size}: {robot_elapsed_time:.2f} seconds.")

        if robot_solved:
            print("Robot successfully solved the problem.")
        else:
            print("Robot failed to solve the problem.")

        # Measure and store the real elapsed time for the professor solver
        professor_start_time = time.time()
        yield self.env.timeout(professor_time)
        print("Professor started solving the problem.")
        professor_solved = professor_solver.solve()
        professor_elapsed_time = time.time() - professor_start_time
        self.elapsed_times["Deterministic"][size].append(
            professor_elapsed_time)
        print(f"Real elapsed time for Deterministic solver on board size {
              size}: {professor_elapsed_time:.2f} seconds.")

        if professor_solved:
            print("Professor successfully solved the problem.")
        else:
            print("Professor failed to solve the problem.")

        # Determine the winner based on whether they solved the problem
        if robot_solved and (not professor_solved or robot_time < professor_time):
            self.profit -= self.penalties  # Decrease profit if the robot wins
            print(f"Robot has won. Profit: {self.profit}")
        elif professor_solved:
            self.profit += self.rewards  # Increase profit if the professor wins
            print(f"Professor has won. Profit: {self.profit}")
        else:
            print(f"No solver could solve the problem. Profit remains: {
                  self.profit}")
