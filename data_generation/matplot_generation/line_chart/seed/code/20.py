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
    df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/user_orders_hourofday.csv")
    df_mean = df.groupby('order_hour_of_day').quantity.mean()
    df_se = df.groupby('order_hour_of_day').quantity.apply(sem).mul(1.96)

    # Plot
    plt.figure(figsize=(16,10), dpi= 80)
    plt.ylabel("# Orders", fontsize=16)
    x = df_mean.index
    plt.plot(x, df_mean, color="white", lw=2)
    plt.fill_between(x, df_mean - df_se, df_mean + df_se, color="#3F5D7D")

    # Decorations
    # Lighten borders
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(1)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    plt.xticks(x[::2], [str(d) for d in x[::2]] , fontsize=12)
    plt.title("User Orders by Hour of Day (95% confidence)", fontsize=22)
    plt.xlabel("Hour of Day")

    s, e = plt.gca().get_xlim()
    plt.xlim(s, e)

    # Draw Horizontal Tick lines
    for y in range(8, 20, 2):
        plt.hlines(y, xmin=s, xmax=e, colors='black', alpha=0.5, linestyles="--", lw=0.5)
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
