
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create dataframe
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Research Papers': [45, 50, 55, 60, 70, 75, 80, 85, 90, 95, 100, 110],
    'Conferences': [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220],
    'Workshops': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]
}
df = pd.DataFrame(data)
df = df.set_index('Month')

# Plot stacked area chart
plt.figure(figsize=(16, 12))
sns.set_theme(style="whitegrid")
pal = ["#FF4500", "#1E90FF", "#3CB371"]

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
    plt.text(df_cum.index[idx], value, f'{df.columns[idx]}: {value}', horizontalalignment='left', size='medium', color=pal[idx])

# Customize chart
plt.title("Annual Academic Activities", fontsize=20, fontweight='bold', pad=20)
plt.xlabel("Month", fontsize=16)
plt.ylabel("Cumulative Count", fontsize=16)
plt.xticks(rotation=45)
plt.legend(title='Activity Type', loc='upper left')

# Show the chart
plt.tight_layout()
plt.show()