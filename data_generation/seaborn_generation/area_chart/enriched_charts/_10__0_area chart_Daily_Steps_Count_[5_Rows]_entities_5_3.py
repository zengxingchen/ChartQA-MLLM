
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Beach': [800, 850, 780, 950, 1200, 1300, 1100],
    'Mountain': [600, 620, 610, 700, 750, 800, 720],
    'Museum': [400, 450, 430, 500, 600, 650, 570],
    'Park': [300, 320, 310, 400, 500, 550, 480]
}

df = pd.DataFrame(data)

# Define the color palette as an array of hex color codes
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

# Plotting the area chart for each attraction
plt.figure(figsize=(12, 8))  # Changed the width and height of the chart
for i, attraction in enumerate(['Beach', 'Mountain', 'Museum', 'Park']):
    ax = sns.lineplot(x='Day', y=attraction, data=df, color=colors[i])
    ax.fill_between(df['Day'], df[attraction], color=colors[i], alpha=0.3)

    # Annotations
    for j, point in df.iterrows():
        ax.text(point['Day'], point[attraction], str(point[attraction]), 
                ha='center', va='bottom')

# Customizing with a title and labels
ax.set_title('Number of Visitors to Different Attractions Over a Week', fontsize=16)
ax.set_xlabel('Day of the Week', fontsize=12)
ax.set_ylabel('Number of Visitors', fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()