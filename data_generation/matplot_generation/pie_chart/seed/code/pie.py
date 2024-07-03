"""
======
pie(x)
======

See `~matplotlib.axes.Axes.pie`.
"""
import matplotlib.pyplot as plt
import numpy as np



import argparse
import os

def save_plot(save_folder, save_filename):

       plt.style.use('_mpl-gallery-nogrid')


       # make data
       x = [1, 2, 3, 4]
       colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

       # plot
       fig, ax = plt.subplots()
       ax.pie(x, colors=colors, radius=3, center=(4, 4),
              wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

       ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
              ylim=(0, 8), yticks=np.arange(1, 8))
       save_path = os.path.join(save_folder, f"{save_filename}.png")
       plt.savefig(save_path)
       plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
