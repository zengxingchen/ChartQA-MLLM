
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Steps': [7000, 8000, 7500, 8200, 9000, 10000, 9500]
}

df = pd.DataFrame(data)

# Define the color palette as an array of hex color codes
colors = ["#4CAF50"]

# Plotting the area chart
plt.figure(figsize=(12, 8))  # Changed the width and height of the chart
ax = sns.lineplot(x='Day', y='Steps', data=df, color=colors[0])
ax.fill_between(df['Day'], df['Steps'], color=colors[0], alpha=0.3)

# Annotations
for i, point in df.iterrows():
    ax.text(point['Day'], point['Steps'], str(point['Steps']), 
            ha='center', va='bottom')

# Customizing with a title and labels
ax.set_title('Daily Step Count Over a Week', fontsize=20)
ax.set_xlabel('Day of the Week', fontsize=14)
ax.set_ylabel('Number of Steps', fontsize=14)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()