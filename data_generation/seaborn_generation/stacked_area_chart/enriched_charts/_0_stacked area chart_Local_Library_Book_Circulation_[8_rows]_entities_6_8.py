
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create dataframe
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'ProductA': [250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360],
    'ProductB': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260],
    'ProductC': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
}
df = pd.DataFrame(data)
df = df.set_index('Month')

# Plot stacked area chart
plt.figure(figsize=(12, 8))
sns.set_theme(style="whitegrid")
pal = ["#1b9e77", "#d95f02", "#7570b3"]

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
plt.title("Monthly Sales Data for Three Products", fontsize=18, fontweight='bold')
plt.xlabel("Month", fontsize=14)
plt.ylabel("Cumulative Sales", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Product')

# Show the chart
plt.tight_layout()
plt.show()