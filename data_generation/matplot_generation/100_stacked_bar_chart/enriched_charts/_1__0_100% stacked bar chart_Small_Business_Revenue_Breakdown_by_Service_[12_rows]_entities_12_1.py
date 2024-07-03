
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    'Technology': [20, 25, 30, 20, 25, 30, 20, 25],
    'Healthcare': [30, 20, 25, 30, 20, 30, 25, 20],
    'Finance': [25, 30, 20, 30, 35, 20, 30, 30],
    'Real Estate': [15, 10, 10, 10, 10, 10, 15, 15],
    'Energy': [10, 15, 15, 10, 10, 10, 10, 10]
}

df = pd.DataFrame(data)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked horizontal bar plot
years = df['Year']
categories = ['Technology', 'Healthcare', 'Finance', 'Real Estate', 'Energy']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

bottom = [0] * len(df)
for category, color in zip(categories, colors):
    values = df[category]
    ax.barh(years, values, left=bottom, label=category, color=color)
    bottom = [i+j for i, j in zip(bottom, values)]

# Title and labels
ax.set_title('Investment Distribution Across Sectors (2015-2022)', fontsize=14, pad=20)
ax.set_xlabel('Percentage (%)')
ax.set_ylabel('Year')
ax.legend(loc='lower right', bbox_to_anchor=(1.15, 0))

# Display the plot
plt.tight_layout()
plt.show()