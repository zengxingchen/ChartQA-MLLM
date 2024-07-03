
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Month': 'January', 'Children': 350, 'Teens': 220, 'Adults': 400, 'Seniors': 180},
    {'Month': 'February', 'Children': 340, 'Teens': 210, 'Adults': 390, 'Seniors': 175},
    # ... all other months ...
    {'Month': 'December', 'Children': 370, 'Teens': 210, 'Adults': 405, 'Seniors': 178}
]

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Convert DataFrame into a format that is suitable for a stacked area chart
df.set_index('Month', inplace=True)
df = df.reindex(pd.date_range(start="2023-01-01", end="2023-12-01", freq='MS').strftime("%B"))
df_cumsum = df.cumsum(axis=1)

# Plotting the areas
fig, ax = plt.subplots(figsize=(12, 7))
pal = sns.color_palette("husl", n_colors=len(df.columns))

# We start at the bottom and draw each layer of the stack
for i, col in enumerate(reversed(df.columns)):
    ax.fill_between(df.index, df_cumsum[col], label=col, color=pal[-(i+1)], alpha=0.8)

# Adding legend in the reverse order to match the stack
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], title='Age Group', bbox_to_anchor=(1.05, 1), loc='upper left')

# Customizing the axes
ax.set_ylabel('Number of Visitors')
ax.set_xlabel('Month')
ax.xaxis.set_major_locator(plt.MaxNLocator(len(df.index)))
ax.set_xticklabels(df.index, rotation=45, ha='right')

# Final touches
sns.despine()
plt.tight_layout()

# Show the plot
plt.show()