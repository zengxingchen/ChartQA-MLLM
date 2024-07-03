"""
=============
scatter(x, y)
=============

See `~matplotlib.axes.Axes.scatter`.
"""


import matplotlib.pyplot as plt
import numpy as np
import argparse
import os
import matplotlib.cbook as cbook
from matplotlib.colors import Normalize
from matplotlib.markers import MarkerStyle
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D
def save_plot(save_folder, save_filename):
    price_data = cbook.get_sample_data('goog.npz')['price_data']
    price_data = price_data[-250:]  # get the most recent 250 trading days

    delta1 = np.diff(price_data["adj_close"]) / price_data["adj_close"][:-1]

    # Marker size in units of points^2
    volume = (15 * price_data["volume"][:-2] / price_data["volume"][0])**2
    close = 0.003 * price_data["close"][:-2] / 0.003 * price_data["open"][:-2]

    fig, ax = plt.subplots()
    ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)

    ax.set_xlabel(r'$\Delta_i$', fontsize=15)
    ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
    ax.set_title('Volume and percent change')

    ax.grid(True)
    fig.tight_layout()
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
