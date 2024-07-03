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
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # Example data
    people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
    y_pos = np.arange(len(people))
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    fig, ax = plt.subplots()

    hbars = ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos, labels=people)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Performance')
    ax.set_title('How fast do you want to go today?')

    # Label with specially formatted floats
    ax.bar_label(hbars, fmt='%.2f')
    ax.set_xlim(right=15)  # adjust xlim to fit labels
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
