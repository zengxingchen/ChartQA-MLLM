
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create dataframe
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Solar': [30, 35, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130],
    'Wind': [60, 65, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],
    'Hydropower': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
}
df = pd.DataFrame(data)
df = df.set_index('Month')

# Plot stacked area chart
plt.figure(figsize=(18, 10))
sns.set_theme(style="whitegrid")
pal = ["#FFD700", "#00BFFF", "#32CD32"]

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
    plt.text(len(df_cum) - 1, value, f'{df.columns[idx]}: {value}', horizontalalignment='left', size='medium', color=pal[idx])

# Customize chart
plt.title("Monthly Renewable Energy Generation", fontsize=20, fontweight='bold', pad=20)
plt.xlabel("Month", fontsize=16)
plt.ylabel("Cumulative Generation (GWh)", fontsize=16)
plt.xticks(rotation=45)
plt.legend(title='Energy Type', loc='upper left')

# Show the chart
plt.tight_layout()
plt.show()