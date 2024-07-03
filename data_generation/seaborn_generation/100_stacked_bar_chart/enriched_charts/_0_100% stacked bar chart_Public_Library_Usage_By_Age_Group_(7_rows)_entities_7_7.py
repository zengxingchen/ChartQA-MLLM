
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data generation from the table
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Electric': [5, 8, 12, 20, 25],
    'Hybrid': [10, 15, 20, 25, 30],
    'Diesel': [40, 35, 30, 25, 20],
    'Petrol': [45, 42, 38, 30, 25]
}
df = pd.DataFrame(data)

# Calculate the percentage of each category
df_pct = df.set_index('Year').apply(lambda x: x / x.sum() * 100, axis=1).reset_index()

# Stacked bar chart
fig, ax = plt.subplots(figsize=(10, 6))  # Change width and height of the chart

colors = ['#348ABD', '#A60628', '#7A68A6', '#467821']  # Modify color scheme using specific color codes

# Plotting
bottom = pd.Series([0] * len(df_pct))
for i, col in enumerate(df.columns[1:]):
    ax.bar(
        df_pct['Year'],
        df_pct[col],
        bottom=bottom,
        color=colors[i],
        edgecolor='white',
        width=0.6,  # Changed width of the bars reasonably
    )
    bottom += df_pct[col]

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Percentage (%)')
plt.title('Market Share of Vehicle Types')

# Change the orientation to horizontal
ax.set_xticks(df_pct['Year'])
ax.set_xticklabels(df_pct['Year'], rotation=0)
ax.legend(df.columns[1:], loc='upper left')

plt.tight_layout()
plt.show()