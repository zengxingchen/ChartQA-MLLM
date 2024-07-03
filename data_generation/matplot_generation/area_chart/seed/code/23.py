import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

from scipy.stats import sem



import argparse
import os

def save_plot(save_folder, save_filename):
        # Import Data
    df = pd.read_csv("https://github.com/selva86/datasets/raw/master/economics.csv")

    # Prepare Data
    x = df['date'].values.tolist()
    y1 = df['psavert'].values.tolist()
    y2 = df['uempmed'].values.tolist()
    mycolors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:brown', 'tab:grey', 'tab:pink', 'tab:olive']
    columns = ['psavert', 'uempmed']

    # Draw Plot
    fig, ax = plt.subplots(1, 1, figsize=(16,9), dpi= 80)
    ax.fill_between(x, y1=y1, y2=0, label=columns[1], alpha=0.5, color=mycolors[1], linewidth=2)
    ax.fill_between(x, y1=y2, y2=0, label=columns[0], alpha=0.5, color=mycolors[0], linewidth=2)

    # Decorations
    ax.set_title('Personal Savings Rate vs Median Duration of Unemployment', fontsize=18)
    ax.set(ylim=[0, 30])
    ax.legend(loc='best', fontsize=12)
    plt.xticks(x[::50], fontsize=10, horizontalalignment='center')
    plt.yticks(np.arange(2.5, 30.0, 2.5), fontsize=10)
    plt.xlim(-10, x[-1])

    # Draw Tick lines
    for y in np.arange(2.5, 30.0, 2.5):
        plt.hlines(y, xmin=0, xmax=len(x), colors='black', alpha=0.3, linestyles="--", lw=0.5)

    # Lighten borders
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(.3)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(.3)
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
