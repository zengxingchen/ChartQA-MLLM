
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2018, 2019, 2020, 2021, 2022, 2023],
    'Apple': [25, 28, 30, 35, 40, 45],
    'Microsoft': [30, 32, 34, 30, 25, 20],
    'Google': [35, 30, 25, 25, 20, 20],
    'Amazon': [10, 10, 11, 10, 15, 15]
}
df = pd.DataFrame(data)

df_pct = df.set_index('Year').apply(lambda x: x / x.sum() * 100, axis=1).reset_index()

fig, ax = plt.subplots(figsize=(10, 14))  # Modified width and height for a vertical chart

colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']  # Changed color scheme

bottom = pd.Series([0] * len(df_pct))
for i, col in enumerate(df.columns[1:]):
    ax.barh(  # Changed to horizontal bar chart
        df_pct['Year'],
        df_pct[col],
        left=bottom,
        color=colors[i],
        edgecolor='white',
        height=0.6  # Adjusted band height
    )
    bottom += df_pct[col]

ax.set_ylabel('Year')
ax.set_xlabel('Percentage (%)')
plt.title('Market Share of Major Tech Companies Over Years', pad=20)  # Updated title with appropriate padding

ax.set_yticks(df_pct['Year'])
ax.set_yticklabels(df_pct['Year'])
ax.legend(df.columns[1:], loc='lower right')  # Moved legend to avoid overlap with title

plt.tight_layout()
plt.show()