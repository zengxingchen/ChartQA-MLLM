
import seaborn as sns
import matplotlib.pyplot as plt

# Data: Daily Hiking Distances
distances = [
    5.2, 7.8, 9.1, 6.4, 8.7, 10.2, 11.5, 9.4, 8.1, 7.3,
    9.6, 6.0, 7.5, 8.7, 11.3, 8.9, 9.8, 8.6, 10.0, 10.2,
    5.9, 6.4, 10.0, 10.1, 9.5, 8.2, 6.8, 7.4, 8.9, 10.5
]

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create a figure and a set of subplots with custom dimensions
plt.figure(figsize=(10, 8))

# Create the histogram with customizations
ax = sns.histplot(distances, bins=10, kde=False, color='#e74c3c', binwidth=0.8, orientation='horizontal')

# Customize the axes labels and the chart title
ax.set_title('Distribution of Daily Hiking Distances', fontsize=16)
ax.set_ylabel('Distance (Kilometers)', fontsize=14)
ax.set_xlabel('Frequency', fontsize=14)

# Finalize and display the plot
plt.tight_layout()
plt.show()