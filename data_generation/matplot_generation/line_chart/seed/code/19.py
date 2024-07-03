import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')



import argparse
import os

def save_plot(save_folder, save_filename):
        # Import Data
    df = pd.read_csv('https://github.com/selva86/datasets/raw/master/mortality.csv')

    # Define the upper limit, lower limit, interval of Y axis and colors
    y_LL = 100
    y_UL = int(df.iloc[:, 1:].max().max()*1.1)
    y_interval = 400
    mycolors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

    # Draw Plot and Annotate
    fig, ax = plt.subplots(1,1,figsize=(16, 9), dpi= 80)

    columns = df.columns[1:]
    for i, column in enumerate(columns):
        plt.plot(df.date.values, df[column].values, lw=1.5, color=mycolors[i])
        plt.text(df.shape[0]+1, df[column].values[-1], column, fontsize=14, color=mycolors[i])

    # Draw Tick lines
    for y in range(y_LL, y_UL, y_interval):
        plt.hlines(y, xmin=0, xmax=71, colors='black', alpha=0.3, linestyles="--", lw=0.5)

    # Decorations
    plt.tick_params(axis="both", which="both", bottom=False, top=False,
                    labelbottom=True, left=False, right=False, labelleft=True)

    # Lighten borders
    plt.gca().spines["top"].set_alpha(.3)
    plt.gca().spines["bottom"].set_alpha(.3)
    plt.gca().spines["right"].set_alpha(.3)
    plt.gca().spines["left"].set_alpha(.3)

    plt.title('Number of Deaths from Lung Diseases in the UK (1974-1979)', fontsize=22)
    plt.yticks(range(y_LL, y_UL, y_interval), [str(y) for y in range(y_LL, y_UL, y_interval)], fontsize=12)
    plt.xticks(range(0, df.shape[0], 12), df.date.values[::12], horizontalalignment='left', fontsize=12)
    plt.ylim(y_LL, y_UL)
    plt.xlim(-2, 80)
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
