
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'Russia', 
                'UK', 'France', 'Italy', 'Canada', 'Brazil', 'Australia'],
    'Medals': [120, 110, 85, 75, 65, 95, 105, 60, 55, 70, 50, 45]
}

# Create DataFrame
df = pd.DataFrame(data)

# seaborn style
sns.set_theme(style="whitegrid")

# Create a color palette
palette = ['#264653', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51', 
           '#8ab17d', '#fe5d26', '#f6bd60', '#6a0572', '#e63946', 
           '#495867', '#ffb4a2']

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 6))

# Plot the Medals
sns.barplot(x="Country", y="Medals", data=df, palette=palette)

# Customize the axes and title
ax.set_xlabel('Country')
ax.set_ylabel('Number of Medals')
ax.set_title('Olympic Medals by Country', pad=20)

# Show values on bars
for p in ax.patches:
    height = p.get_height()
    plt.text(p.get_x() + p.get_width() / 2., height + 2,
             '{:1.0f}'.format(height),
             ha='center', va='center')

# Set the band width
ax.bar_label(ax.containers[0], label_type='center')

# Set the margins
plt.subplots_adjust(left=0.1, right=0.95, top=0.85, bottom=0.15)

# Show the plot
plt.show()