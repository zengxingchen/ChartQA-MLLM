
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data generation from the table
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Research': [10, 15, 20, 30, 40],
    'Development': [20, 25, 30, 35, 30],
    'Production': [30, 35, 25, 20, 20],
    'Marketing': [40, 25, 25, 15, 10]
}
df = pd.DataFrame(data)

# Calculate the percentage of each category
df_pct = df.set_index('Year').apply(lambda x: x / x.sum() * 100, axis=1).reset_index()

# Stacked bar chart
fig, ax = plt.subplots(figsize=(8, 12))  # Change width and height of the chart

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']  # Modify color scheme using specific color codes

# Plotting
bottom = pd.Series([0] * len(df_pct))
for i, col in enumerate(df.columns[1:]):
    ax.bar(
        df_pct['Year'],
        df_pct[col],
        bottom=bottom,
        color=colors[i],
        edgecolor='white',
        width=0.5,  # Changed width of the bars reasonably
    )
    bottom += df_pct[col]

# Adding labels and title
ax.set_xlabel('Percentage (%)')
ax.set_ylabel('Year')
plt.title('Budget Allocation in R&D Department')

# Change the orientation to vertical
ax.set_yticks(df_pct['Year'])
ax.set_yticklabels(df_pct['Year'], rotation=0)
ax.legend(df.columns[1:], loc='upper right')

plt.tight_layout()
plt.show()