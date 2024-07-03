
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create dataframe
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'News Articles': [80, 70, 60, 90, 80, 70, 100, 90, 80, 110, 100, 90],
    'TV Shows': [130, 120, 110, 140, 130, 120, 150, 140, 130, 160, 150, 140],
    'Movies': [180, 170, 160, 190, 180, 170, 200, 190, 180, 210, 200, 190]
}
df = pd.DataFrame(data)
df = df.set_index('Month')

# Plot stacked area chart
plt.figure(figsize=(14, 10))
sns.set_theme(style="whitegrid")
pal = ["#FF6347", "#4682B4", "#32CD32"]

# Cumulate the values
df_cum = df.cumsum(axis=1)

# Plot the lines to create a stacked effect
for i in range(len(df.columns)-1, -1, -1):
    sns.lineplot(data=df_cum[df.columns[i]], label=df.columns[i], color=pal[i], linewidth=0)

# Fill the area between the lines
for i in range(len(df.columns)-1):
    plt.fill_between(df.index, df_cum.iloc[:, i], df_cum.iloc[:, i+1], facecolor=pal[i], alpha=0.7)

# Annotation
for idx, value in enumerate(df_cum.iloc[-1]):
    plt.text(idx, value, f'{df.columns[idx]}: {value}', horizontalalignment='left', size='medium', color=pal[idx])

# Customize chart
plt.title("Monthly Media Consumption", fontsize=18, fontweight='bold')
plt.xlabel("Month", fontsize=14)
plt.ylabel("Cumulative Count", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Media Type')

# Show the chart
plt.tight_layout()
plt.show()