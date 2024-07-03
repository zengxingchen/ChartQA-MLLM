
import seaborn as sns
import matplotlib.pyplot as plt

# Data: Average Monthly Internet Usage (GB)
internet_usage = [
    25.4, 30.2, 45.6, 32.1, 27.5, 38.3, 50.7, 34.9, 40.5, 29.3,
    33.8, 47.2, 55.0, 61.4, 48.9, 53.3
]

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create a figure and a set of subplots with custom dimensions
plt.figure(figsize=(12, 6))

# Create the histogram with customizations
ax = sns.histplot(internet_usage, bins=6, kde=False, color='#FF6347', binwidth=5)

# Customize the axes labels and the chart title
ax.set_title('Distribution of Average Monthly Internet Usage', fontsize=18, loc='right')
ax.set_xlabel('Internet Usage (GB)', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

# Finalize and display the plot
plt.tight_layout()
plt.show()