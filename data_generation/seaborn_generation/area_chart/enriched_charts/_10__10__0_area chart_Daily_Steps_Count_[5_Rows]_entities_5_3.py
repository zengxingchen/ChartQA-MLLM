
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Activity': ['Study', 'Exercise', 'Work', 'Relax', 'Socialize', 'Recreation', 'Rest'],
    'Hours_Slept': [6.5, 7, 5.5, 8, 6, 8.5, 7.5]
}

df = pd.DataFrame(data)

# Define the color palette as an array of hex color codes
colors = ["#ff6347"]

# Plotting the area chart
plt.figure(figsize=(10, 6))  # Changed the width and height of the chart
ax = sns.lineplot(x='Day', y='Hours_Slept', data=df, color=colors[0])
ax.fill_between(df['Day'], df['Hours_Slept'], color=colors[0], alpha=0.3)

# Annotations
for i, point in df.iterrows():
    ax.text(point['Day'], point['Hours_Slept'], str(point['Hours_Slept']), 
            ha='center', va='bottom')

# Customizing with a title and labels
ax.set_title('Hours of Sleep Over a Week', fontsize=16, pad=20)
ax.set_xlabel('Day of the Week', fontsize=12)
ax.set_ylabel('Hours Slept', fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()