"""
==========================
Labeling a pie and a donut
==========================

Welcome to the Matplotlib bakery. We will create a pie and a donut
chart through the `pie method <matplotlib.axes.Axes.pie>` and
show how to label them with a `legend <matplotlib.axes.Axes.legend>`
as well as with `annotations <matplotlib.axes.Axes.annotate>`.
"""

# %%
# As usual we would start by defining the imports and create a figure with
# subplots.
# Now it's time for the pie. Starting with a pie recipe, we create the data
# and a list of labels from it.
#
# We can provide a function to the ``autopct`` argument, which will expand
# automatic percentage labeling by showing absolute values; we calculate
# the latter back from relative data and the known sum of all values.
#
# We then create the pie and store the returned objects for later.  The first
# returned element of the returned tuple is a list of the wedges.  Those are
# `matplotlib.patches.Wedge` patches, which can directly be used as the handles
# for a legend. We can use the legend's ``bbox_to_anchor`` argument to position
# the legend outside of the pie. Here we use the axes coordinates ``(1, 0, 0.5,
# 1)`` together with the location ``"center left"``; i.e. the left central
# point of the legend will be at the left central point of the bounding box,
# spanning from ``(1, 0)`` to ``(1.5, 1)`` in axes coordinates.

import matplotlib.pyplot as plt
import numpy as np





# %%
# And here it is, the donut. Note however, that if we were to use this recipe,
# the ingredients would suffice for around 6 donuts - producing one huge
# donut is untested and might result in kitchen errors.


# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.pie` / `matplotlib.pyplot.pie`
#    - `matplotlib.axes.Axes.legend` / `matplotlib.pyplot.legend`

import argparse
import os

def save_plot(save_folder, save_filename):
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    recipe = ["225 g flour",
            "90 g sugar",
            "1 egg",
            "60 g butter",
            "100 ml milk",
            "1/2 package of yeast"]

    data = [225, 90, 50, 60, 100, 5]

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
            bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={ang}"
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)

    ax.set_title("Matplotlib bakery: A donut")
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
