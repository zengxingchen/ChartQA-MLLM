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
    df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/nightvisitors.csv')

    # Decide Colors
    mycolors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:brown', 'tab:grey', 'tab:pink', 'tab:olive']

    # Draw Plot and Annotate
    fig, ax = plt.subplots(1,1,figsize=(16, 9), dpi= 80)
    columns = df.columns[1:]
    labs = columns.values.tolist()

    # Prepare data
    x  = df['yearmon'].values.tolist()
    y0 = df[columns[0]].values.tolist()
    y1 = df[columns[1]].values.tolist()
    y2 = df[columns[2]].values.tolist()
    y3 = df[columns[3]].values.tolist()
    y4 = df[columns[4]].values.tolist()
    y5 = df[columns[5]].values.tolist()
    y6 = df[columns[6]].values.tolist()
    y7 = df[columns[7]].values.tolist()
    y = np.vstack([y0, y2, y4, y6, y7, y5, y1, y3])

    # Plot for each column
    labs = columns.values.tolist()
    ax = plt.gca()
    ax.stackplot(x, y, labels=labs, colors=mycolors, alpha=0.8)

    # Decorations
    ax.set_title('Night Visitors in Australian Regions', fontsize=18)
    ax.set(ylim=[0, 100000])
    ax.legend(fontsize=10, ncol=4)
    plt.xticks(x[::5], fontsize=10, horizontalalignment='center')
    plt.yticks(np.arange(10000, 100000, 20000), fontsize=10)
    plt.xlim(x[0], x[-1])

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
