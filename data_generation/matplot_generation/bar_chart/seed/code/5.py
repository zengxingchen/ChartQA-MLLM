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
    df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")
    x = df.loc[:, ['mpg']]
    df['mpg_z'] = (x - x.mean())/x.std()
    df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]
    df.sort_values('mpg_z', inplace=True)
    df.reset_index(inplace=True)

    # Draw plot
    plt.figure(figsize=(14,10), dpi= 80)
    plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z, color=df.colors, alpha=0.4, linewidth=5)

    # Decorations
    plt.gca().set(ylabel='$Model$', xlabel='$Mileage$')
    plt.yticks(df.index, df.cars, fontsize=12)
    plt.title('Diverging Bars of Car Mileage', fontdict={'size':20})
    plt.grid(linestyle='--', alpha=0.5)
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
