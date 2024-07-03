
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create dataframe
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Exercise': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210],
    'Reading': [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135],
    'Socializing': [90, 95, 100, 110, 115, 120, 125, 130, 135, 140, 145, 150]
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
plt.title("Monthly Time Spent on Activities", fontsize=18, fontweight='bold', loc='left')
plt.xlabel("Month", fontsize=14)
plt.ylabel("Cumulative Hours", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Activity', loc='upper right')

# Show the chart
plt.tight_layout()
plt.show()