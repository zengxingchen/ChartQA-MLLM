import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')



import argparse
import os

def save_plot(save_folder, save_filename):
    # Prepare Data
    df_raw = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
    df = df_raw[['cty', 'manufacturer']].groupby('manufacturer').apply(lambda x: x.mean())
    df.sort_values('cty', inplace=True)
    df.reset_index(inplace=True)

    # Draw plot
    import matplotlib.patches as patches

    fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
    ax.vlines(x=df.index, ymin=0, ymax=df.cty, color='firebrick', alpha=0.7, linewidth=20)

    # Annotate Text
    for i, cty in enumerate(df.cty):
        ax.text(i, cty+0.5, round(cty, 1), horizontalalignment='center')


    # Title, Label, Ticks and Ylim
    ax.set_title('Bar Chart for Highway Mileage', fontdict={'size':22})
    ax.set(ylabel='Miles Per Gallon', ylim=(0, 30))
    plt.xticks(df.index, df.manufacturer.str.upper(), rotation=60, horizontalalignment='right', fontsize=12)

    # Add patches to color the X axis labels
    p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
    p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
    fig.add_artist(p1)
    fig.add_artist(p2)
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
