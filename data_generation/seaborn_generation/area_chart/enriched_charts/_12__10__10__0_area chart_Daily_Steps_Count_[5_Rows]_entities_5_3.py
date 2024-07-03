
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Category': ['Science & Nature'] * 7,
    'Views': [120, 135, 150, 145, 160, 170, 155]
}

df = pd.DataFrame(data)

# Define the color palette as an array of hex color codes
colors = ["#4682B4"]

# Plotting the area chart
plt.figure(figsize=(12, 8))  # Changed the width and height of the chart
ax = sns.lineplot(x='Day', y='Views', data=df, color=colors[0])
ax.fill_between(df['Day'], df['Views'], color=colors[0], alpha=0.4)

# Annotations
for i, point in df.iterrows():
    ax.text(point['Day'], point['Views'], str(point['Views']), 
            ha='center', va='bottom')

# Customizing with a title and labels
ax.set_title('Daily Views on Science & Nature Articles', fontsize=18, pad=20)
ax.set_xlabel('Day of the Week', fontsize=14)
ax.set_ylabel('Views', fontsize=14)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()