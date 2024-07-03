"""
.. redirect-from:: gallery/pie_and_polar_charts/pie_demo2

==========
Pie charts
==========

Demo of plotting a pie chart.

This example illustrates various parameters of `~matplotlib.axes.Axes.pie`.
"""

# %%
# Label slices
# ------------
#
# Plot a pie chart of animals and label the slices. To add
# labels, pass a list of labels to the *labels* parameter

import matplotlib.pyplot as plt




import argparse
import os

def save_plot(save_folder, save_filename):
    
       labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
       sizes = [15, 30, 45, 10]

       fig, ax = plt.subplots()
       ax.pie(sizes, labels=labels)
       save_path = os.path.join(save_folder, f"{save_filename}.png")
       plt.savefig(save_path)
       plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
