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
    species = ('Adelie', 'Chinstrap', 'Gentoo')
    sex_counts = {
        'Male': np.array([73, 34, 61]),
        'Female': np.array([73, 34, 58]),
    }
    width = 0.6  # the width of the bars: can also be len(x) sequence


    fig, ax = plt.subplots()
    bottom = np.zeros(3)

    for sex, sex_count in sex_counts.items():
        p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
        bottom += sex_count

        ax.bar_label(p, label_type='center')

    ax.set_title('Number of penguins by sex')
    ax.legend()
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
