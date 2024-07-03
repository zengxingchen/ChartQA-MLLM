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




import argparse
import os

def save_plot(save_folder, save_filename):
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    recipe = ["375 g flour",
            "75 g sugar",
            "250 g butter",
            "300 g berries"]

    data = [float(x.split()[0]) for x in recipe]
    ingredients = [x.split()[-1] for x in recipe]


    def func(pct, allvals):
        absolute = int(np.round(pct/100.*np.sum(allvals)))
        return f"{pct:.1f}%\n({absolute:d} g)"


    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                    textprops=dict(color="w"))

    ax.legend(wedges, ingredients,
            title="Ingredients",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title("Matplotlib bakery: A pie")
    save_path = os.path.join(save_folder, f"{save_filename}.png")
    plt.savefig(save_path)
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save a matplotlib plot.")
    parser.add_argument("save_folder", help="The folder path where the plot will be saved.")
    parser.add_argument("save_filename", help="The file name for the saved plot, without extension.")
    
    args = parser.parse_args()
    save_plot(args.save_folder, args.save_filename)
