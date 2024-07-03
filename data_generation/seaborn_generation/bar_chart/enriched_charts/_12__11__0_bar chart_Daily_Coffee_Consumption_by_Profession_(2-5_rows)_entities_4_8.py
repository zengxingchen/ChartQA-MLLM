
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'Russia', 
                'UK', 'France', 'Italy', 'Canada', 'Brazil', 'Australia'],
    'Books Read': [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 8, 12]
}

# Create DataFrame
df = pd.DataFrame(data)

# seaborn style
sns.set_theme(style="whitegrid")

# Create a color palette
palette = ['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', 
           '#f95d6a', '#ff7c43', '#ffa600', '#003f5c', '#2f4b7c', 
           '#665191', '#a05195']

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(8, 12))

# Plot the Books Read
sns.barplot(y="Country", x="Books Read", data=df, palette=palette, ci=None)

# Customize the axes and title
ax.set_ylabel('Country')
ax.set_xlabel('Books Read')
ax.set_title('Books Read by Country in 2023', pad=20)

# Show values on bars
for p in ax.patches:
    width = p.get_width()
    plt.text(width + 1, p.get_y() + p.get_height() / 2.,
             '{:1.0f}'.format(width),
             ha='center', va='center')

# Set the band width
ax.bar_label(ax.containers[0], label_type='center')

# Set the margins
plt.subplots_adjust(left=0.15, right=0.9, top=0.85, bottom=0.15)

# Show the plot
plt.show()