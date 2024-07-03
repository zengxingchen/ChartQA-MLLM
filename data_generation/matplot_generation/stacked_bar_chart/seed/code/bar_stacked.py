"""
=================
Stacked bar chart
=================

This is an example of creating a stacked bar plot
using `~matplotlib.pyplot.bar`.
"""

import matplotlib.pyplot as plt
import numpy as np

# data from https://allisonhorst.github.io/palmerpenguins/





import argparse
import os

def save_plot(save_folder, save_filename):
    species = (
        "Adelie\n $\\mu=$3700.66g",
        "Chinstrap\n $\\mu=$3733.09g",
        "Gentoo\n $\\mu=5076.02g$",
    )
    weight_counts = {
        "Below": np.array([70, 31, 58]),
        "Above": np.array([82, 37, 66]),
    }
    width = 0.5

    fig, ax = plt.subplots()
    bottom = np.zeros(3)

    for boolean, weight_count in weight_counts.items():
        p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
        bottom += weight_count

    ax.set_title("Number of penguins with above average body mass")
    ax.legend(loc="upper right")
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
