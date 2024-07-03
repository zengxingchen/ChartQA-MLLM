
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales': [4500, 4700, 5200, 5800, 6100, 6300, 6600, 7000, 7200, 7500, 7700, 8000]
}

df = pd.DataFrame(data)

# Define the color palette as an array of hex color codes
colors = ["#2e8b57"]

# Plotting the area chart
plt.figure(figsize=(12, 7))  # Changed the width and height of the chart
ax = sns.lineplot(x='Month', y='Sales', data=df, color=colors[0])
ax.fill_between(df['Month'], df['Sales'], color=colors[0], alpha=0.3)

# Annotations
for i, point in df.iterrows():
    ax.text(point['Month'], point['Sales'], str(point['Sales']), 
            ha='center', va='bottom')

# Customizing with a title and labels
ax.set_title('Monthly Sales Over a Year', fontsize=16, pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Sales', fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()