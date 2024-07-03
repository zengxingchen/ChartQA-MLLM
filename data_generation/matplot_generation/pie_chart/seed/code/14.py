import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}% ({:d} )".format(pct, absolute)


import argparse
import os

def save_plot(save_folder, save_filename):
    # Import
    df_raw = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

    # Prepare Data
    df = df_raw.groupby('class').size().reset_index(name='counts')

    # Draw Plot
    fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi= 80)

    data = df['counts']
    categories = df['class']
    explode = [0,0,0,0,0,0.1,0]



    wedges, texts, autotexts = ax.pie(data,
                                    autopct=lambda pct: func(pct, data),
                                    textprops=dict(color="w"),
                                    colors=plt.cm.Dark2.colors,
                                    startangle=140,
                                    explode=explode)

    # Decoration
    ax.legend(wedges, categories, title="Vehicle Class", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=10, weight=700)
    ax.set_title("Class of Vehicles: Pie Chart")
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
