"""
=======
hist(x)
=======

See `~matplotlib.axes.Axes.hist`.
"""
import matplotlib.pyplot as plt
import numpy as np





import argparse
import os

def save_plot(save_folder, save_filename):
    plt.style.use('_mpl-gallery')

    # make data
    np.random.seed(1)
    x = 4 + np.random.normal(0, 1.5, 200)

    # plot:
    fig, ax = plt.subplots()

    ax.hist(x, bins=8, linewidth=0.5, edgecolor="white")

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
        ylim=(0, 56), yticks=np.linspace(0, 56, 9))
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
