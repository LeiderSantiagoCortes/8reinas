import matplotlib.pyplot as plt
import numpy as np


def plot_elapsed_times(elapsed_times, board_sizes):
    """
    Plots the elapsed times for each board size for both Las Vegas and Deterministic solvers.

    Args:
        elapsed_times (dict): Dictionary containing elapsed times for both solvers.
        board_sizes (list): List of board sizes.
    """
    bar_width = 0.35
    index = np.arange(len(board_sizes))

    avg_times_lv = [sum(times) / len(times)
                    if times else 0 for times in elapsed_times["LasVegas"].values()]
    avg_times_det = [sum(times) / len(times)
                     if times else 0 for times in elapsed_times["Deterministic"].values()]

    plt.bar(index, avg_times_lv, bar_width, label='Robot')
    plt.bar(index + bar_width, avg_times_det, bar_width, label='Professor')

    plt.xlabel('Board Size')
    plt.ylabel('Average Elapsed Time (seconds)')
    plt.title('Average Elapsed Time by Board Size and Solver')
    plt.xticks(index + bar_width / 2, board_sizes)
    plt.legend()
    plt.tight_layout()
    plt.show()
