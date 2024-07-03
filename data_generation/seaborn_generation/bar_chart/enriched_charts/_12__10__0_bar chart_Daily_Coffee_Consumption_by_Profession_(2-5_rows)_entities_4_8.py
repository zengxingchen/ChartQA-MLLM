
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Category': ['Ancient Ruins', 'Historical Monuments', 'Museums', 'Archaeological Sites', 'Cultural Heritage',
                 'Landmarks', 'Heritage Trails', 'Historical Cities', 'Medieval Castles', 'Ancient Temples', 'Artifacts', 'Historical Tours'],
    'Value': [80, 95, 120, 150, 130, 140, 110, 160, 135, 125, 145, 155]
}

# Create DataFrame
df = pd.DataFrame(data)

# seaborn style
sns.set_theme(style="whitegrid")

# Create a color palette
palette = ['#4B0082', '#483D8B', '#6A5ACD', '#7B68EE', '#9370DB', '#8A2BE2', '#9400D3', '#9932CC', '#BA55D3', '#DA70D6', '#EE82EE', '#DDA0DD']

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 8))

# Plot the data
sns.barplot(y="Category", x="Value", data=df, palette=palette, width=0.6)

# Customize the axes and title
ax.set_xlabel('Popularity Index')
ax.set_ylabel('Category')
ax.set_title('Historical Sites and Their Popularity Index', fontsize=16, pad=20)

# Show values on bars
for p in ax.patches:
    width = p.get_width()
    plt.text(width + 1, p.get_y() + p.get_height() / 2,
             '{:1.0f}'.format(width),
             ha='center', va='center')

# Set the margins
plt.subplots_adjust(left=0.25, right=0.95, top=0.90, bottom=0.15)

# Show the plot
plt.show()