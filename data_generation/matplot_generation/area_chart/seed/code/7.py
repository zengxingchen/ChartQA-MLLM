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
    df = pd.read_csv("https://github.com/selva86/datasets/raw/master/economics.csv", parse_dates=['date']).head(100)
    x = np.arange(df.shape[0])
    y_returns = (df.psavert.diff().fillna(0)/df.psavert.shift(1)).fillna(0) * 100

    # Plot
    plt.figure(figsize=(16,10), dpi= 80)
    plt.fill_between(x[1:], y_returns[1:], 0, where=y_returns[1:] >= 0, facecolor='green', interpolate=True, alpha=0.7)
    plt.fill_between(x[1:], y_returns[1:], 0, where=y_returns[1:] <= 0, facecolor='red', interpolate=True, alpha=0.7)

    # Annotate
    plt.annotate('Peak \n1975', xy=(94.0, 21.0), xytext=(88.0, 28),
                bbox=dict(boxstyle='square', fc='firebrick'),
                arrowprops=dict(facecolor='steelblue', shrink=0.05), fontsize=15, color='white')


    # Decorations
    xtickvals = [str(m)[:3].upper()+"-"+str(y) for y,m in zip(df.date.dt.year, df.date.dt.month_name())]
    plt.gca().set_xticks(x[::6])
    plt.gca().set_xticklabels(xtickvals[::6], rotation=90, fontdict={'horizontalalignment': 'center', 'verticalalignment': 'center_baseline'})
    plt.ylim(-35,35)
    plt.xlim(1,100)
    plt.title("Month Economics Return %", fontsize=22)
    plt.ylabel('Monthly returns %')
    plt.grid(alpha=0.5)
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
