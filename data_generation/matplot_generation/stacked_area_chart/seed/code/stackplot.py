"""
===============
stackplot(x, y)
===============
See `~matplotlib.axes.Axes.stackplot`
"""



import matplotlib.pyplot as plt
import numpy as np
import argparse
import os

def save_plot(save_folder, save_filename):


    plt.style.use('_mpl-gallery')

    # make data
    x = np.arange(0, 10, 2)
    ay = [1, 1.25, 2, 2.75, 3]
    by = [1, 1, 1, 1, 1]
    cy = [2, 1, 2, 1, 2]
    y = np.vstack([ay, by, cy])

    # plot
    fig, ax = plt.subplots()

    ax.stackplot(x, y)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
        ylim=(0, 8), yticks=np.arange(1, 8))
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
