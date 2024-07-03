
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Books Sold': [120, 150, 170, 160, 180, 220, 210]
}

df = pd.DataFrame(data)

# Define the color palette as an array of hex color codes
colors = ["#FF6347"]

# Plotting the area chart
plt.figure(figsize=(10, 6))  # Changed the width and height of the chart
ax = sns.lineplot(x='Day', y='Books Sold', data=df, color=colors[0])
ax.fill_between(df['Day'], df['Books Sold'], color=colors[0], alpha=0.3)

# Annotations
for i, point in df.iterrows():
    ax.text(point['Day'], point['Books Sold'], str(point['Books Sold']), 
            ha='center', va='bottom')

# Customizing with a title and labels
ax.set_title('Books Sold Over a Week', fontsize=18)
ax.set_xlabel('Day of the Week', fontsize=14)
ax.set_ylabel('Number of Books Sold', fontsize=14)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()