"""
=================
Nested pie charts
=================

The following examples show two ways to build a nested pie chart
in Matplotlib. Such charts are often referred to as donut charts.

See also the :doc:`/gallery/specialty_plots/leftventricle_bullseye` example.
"""

import matplotlib.pyplot as plt
import numpy as np

# %%
# The most straightforward way to build a pie chart is to use the
# `~matplotlib.axes.Axes.pie` method.
#
# In this case, pie takes values corresponding to counts in a group.
# We'll first generate some fake data, corresponding to three groups.
# In the inner circle, we'll treat each number as belonging to its
# own group. In the outer circle, we'll plot them as members of their
# original 3 groups.
#
# The effect of the donut shape is achieved by setting a ``width`` to
# the pie's wedges through the *wedgeprops* argument.





import argparse
import os

def save_plot(save_folder, save_filename):
       fig, ax = plt.subplots()

       size = 0.3
       vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

       cmap = plt.colormaps["tab20c"]
       outer_colors = cmap(np.arange(3)*4)
       inner_colors = cmap([1, 2, 5, 6, 9, 10])

       ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
              wedgeprops=dict(width=size, edgecolor='w'))

       ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
              wedgeprops=dict(width=size, edgecolor='w'))

       ax.set(aspect="equal", title='Pie plot with `ax.pie`')
       save_path = os.path.join(save_folder, f"{save_filename}.png")
       plt.savefig(save_path)
       plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
