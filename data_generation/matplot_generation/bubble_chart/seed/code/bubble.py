"""
=============
scatter(x, y)
=============

See `~matplotlib.axes.Axes.scatter`.
"""


import matplotlib.pyplot as plt
import numpy as np
import argparse
import os
from matplotlib.colors import Normalize
from matplotlib.markers import MarkerStyle
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D
def save_plot(save_folder, save_filename):
    SUCCESS_SYMBOLS = [
        TextPath((0, 0), "☹"),
        TextPath((0, 0), "😒"),
        TextPath((0, 0), "☺"),
    ]

    N = 25
    np.random.seed(42)
    skills = np.random.uniform(5, 80, size=N) * 0.1 + 5
    takeoff_angles = np.random.normal(0, 90, N)
    thrusts = np.random.uniform(size=N)
    successful = np.random.randint(0, 3, size=N)
    positions = np.random.normal(size=(N, 2)) * 5
    data = zip(skills, takeoff_angles, thrusts, successful, positions)

    cmap = plt.colormaps["plasma"]
    fig, ax = plt.subplots()
    fig.suptitle("Throwing success", size=14)
    for skill, takeoff, thrust, mood, pos in data:
        t = Affine2D().scale(skill).rotate_deg(takeoff)
        m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t)
        ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust))
    fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(0, 1), cmap=cmap),
                ax=ax, label="Normalized Thrust [a.u.]")
    ax.set_xlabel("X position [m]")
    ax.set_ylabel("Y position [m]")
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
