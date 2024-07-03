import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

import random



import argparse
import os

def save_plot(save_folder, save_filename):
        # Import Data
    df_raw = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

    # Prepare Data
    df = df_raw.groupby('manufacturer').size().reset_index(name='counts')
    n = df['manufacturer'].unique().__len__()+1
    all_colors = list(plt.cm.colors.cnames.keys())
    random.seed(100)
    c = random.choices(all_colors, k=n)

    # Plot Bars
    plt.figure(figsize=(16,10), dpi= 80)
    plt.bar(df['manufacturer'], df['counts'], color=c, width=.5)
    for i, val in enumerate(df['counts'].values):
        plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':12})

    # Decoration
    plt.gca().set_xticklabels(df['manufacturer'], rotation=60, horizontalalignment= 'right')
    plt.title("Number of Vehicles by Manaufacturers", fontsize=22)
    plt.ylabel('# Vehicles')
    plt.ylim(0, 45)
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
