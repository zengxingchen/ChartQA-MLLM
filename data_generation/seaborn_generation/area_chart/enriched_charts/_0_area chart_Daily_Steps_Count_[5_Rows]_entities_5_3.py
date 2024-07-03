
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Visitors': [1200, 1350, 1230, 1400, 1550, 1600, 1450]
}

df = pd.DataFrame(data)

# Define the color palette as an array of hex color codes
colors = ["#FF5733"]

# Plotting the area chart
plt.figure(figsize=(10, 6))  # Changed the width and height of the chart
ax = sns.lineplot(x='Day', y='Visitors', data=df, color=colors[0])
ax.fill_between(df['Day'], df['Visitors'], color=colors[0], alpha=0.3)

# Annotations
for i, point in df.iterrows():
    ax.text(point['Day'], point['Visitors'], str(point['Visitors']), 
            ha='center', va='bottom')

# Customizing with a title and labels
ax.set_title('Website Visitors Trend Over a Week', fontsize=16)
ax.set_xlabel('Day of the Week', fontsize=12)
ax.set_ylabel('Number of Visitors', fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()