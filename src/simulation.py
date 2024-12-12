from typing import Generator

# import time
# from solver_robot import LasVegasSolver
# from solver_professor import DeterministicSolver

import simpy
import random

# Input variables
BOARD_SIZES = [4, 5, 6, 8, 10, 12, 15]  # possible board sizes
ROBOT_ARRIVAL_TIME_RANGE = (10, 30)  # arrival time range for robots in seconds
SIMULATION_DURATION = 8 * 60 * 60  # 8 hours in seconds

# Performance variables
profit = 0
total_games = 0
games_won_by_robot = 0
games_won_by_professor = 0


def solve_problem_robot(n: int) -> float:
    # Las Vegas algorithm (simulated resolution time)
    return random.uniform(1, 5)  # Fictitious time from 1 to 5 seconds


def solve_problem_professor(n: int) -> float:
    # Deterministic algorithm (simulated resolution time)
    return n * 0.5  # Fictitious time based on board size


def game_simulation(env: simpy.Environment) -> Generator:
    """
    Simulates a game environment where a robot and a professor compete to solve a problem.
    The function continuously generates arrival times for robots, selects a board size,
    calculates the resolution times for both the robot and the professor, and determines
    the winner of each game. The results are used to update global statistics such as profit,
    total games played, and the number of games won by the robot and the professor.
    Args:
        env (simpy.Environment): The simulation environment.
    Yields:
        simpy.events.Timeout: A timeout event for the arrival of the next robot.
    """
    global profit, total_games, games_won_by_robot, games_won_by_professor

    while True:
        # Generate the arrival time of the next robot
        yield env.timeout(random.uniform(*ROBOT_ARRIVAL_TIME_RANGE))

        # Select the board size
        n = random.choice(BOARD_SIZES)

        # Calculate the resolution time for the robot and the professor
        robot_time = solve_problem_robot(n)
        professor_time = solve_problem_professor(n)

        # Determine the winner of the game
        total_games += 1
        if robot_time < professor_time:
            profit -= 10
            games_won_by_robot += 1
        else:
            profit += 15
            games_won_by_professor += 1
