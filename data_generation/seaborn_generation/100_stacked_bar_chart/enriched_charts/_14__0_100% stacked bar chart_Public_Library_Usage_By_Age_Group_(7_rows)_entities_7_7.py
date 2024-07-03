
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data generation from the table
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Smartphones': [15, 20, 25, 30, 35],
    'Laptops': [25, 22, 20, 25, 28],
    'Tablets': [20, 25, 30, 27, 22],
    'Desktops': [40, 33, 25, 18, 15]
}
df = pd.DataFrame(data)

# Calculate the percentage of each category
df_pct = df.set_index('Year').apply(lambda x: x / x.sum() * 100, axis=1).reset_index()

# Stacked bar chart
fig, ax = plt.subplots(figsize=(8, 10))  # Change width and height of the chart

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Modify color scheme using specific color codes

# Plotting
bottom = pd.Series([0] * len(df_pct))
for i, col in enumerate(df.columns[1:]):
    ax.barh(
        df_pct['Year'],
        df_pct[col],
        left=bottom,
        color=colors[i],
        edgecolor='white',
        height=0.5,  # Changed height of the bars reasonably
    )
    bottom += df_pct[col]

# Adding labels and title
ax.set_ylabel('Year')
ax.set_xlabel('Percentage (%)')
plt.title('Market Share of Computing Devices')

# Change the orientation to horizontal
ax.set_yticks(df_pct['Year'])
ax.set_yticklabels(df_pct['Year'], rotation=0)
ax.legend(df.columns[1:], loc='upper right')

plt.tight_layout()
plt.show()