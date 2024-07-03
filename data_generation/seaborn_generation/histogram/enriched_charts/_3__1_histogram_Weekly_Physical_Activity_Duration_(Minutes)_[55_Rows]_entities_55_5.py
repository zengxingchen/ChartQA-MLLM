
import seaborn as sns
import matplotlib.pyplot as plt

# Data: Average Monthly Rainfall (mm)
rainfall = [
    78.5, 64.2, 85.6, 92.1, 110.5, 125.3, 142.8, 130.7, 115.4, 100.6, 88.3, 75.9
]

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create a figure and a set of subplots with custom dimensions
plt.figure(figsize=(10, 8))

# Create the histogram with customizations
ax = sns.histplot(rainfall, bins=8, kde=False, color='#1f77b4', binwidth=10)

# Customize the axes labels and the chart title
ax.set_title('Distribution of Average Monthly Rainfall', fontsize=18, loc='left')
ax.set_xlabel('Rainfall (mm)', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

# Rotate the plot to horizontal
plt.gca().invert_yaxis()

# Finalize and display the plot
plt.tight_layout()
plt.show()