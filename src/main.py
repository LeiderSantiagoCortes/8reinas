from simulation import (
    profit,
    total_games,
    games_won_by_robot,
    games_won_by_professor,
    SIMULATION_DURATION,
    game_simulation,
)
import simpy


def main() -> None:
    global profit, total_games, games_won_by_robot, games_won_by_professor

    # Create the SimPy environment
    env = simpy.Environment()

    # Start the game simulation process
    env.process(game_simulation(env))

    # Run the simulation for the specified duration
    env.run(until=SIMULATION_DURATION)

    # Display the results
    print(f"Total profit: {profit}")
    print(f"Total games: {total_games}")
    print(f"Games won by the robot: {games_won_by_robot}")
    print(f"Games won by the professor: {games_won_by_professor}")


if __name__ == "__main__":
    main()
