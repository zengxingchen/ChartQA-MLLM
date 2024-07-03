
import seaborn as sns
import matplotlib.pyplot as plt

# Data: Daily Maximum Temperatures
temperatures = [
    22.5, 19.3, 25.1, 21.4, 28.7, 30.2, 31.5, 29.4, 26.8, 24.1,
    27.3, 20.6, 23.5, 25.7, 29.8, 24.9, 28.1, 26.6, 27.0, 29.2,
    21.2, 22.4, 30.0, 31.1, 27.5, 26.2, 20.8, 23.7, 25.9, 28.3
]

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create a figure and a set of subplots with custom dimensions
plt.figure(figsize=(12, 6))

# Create the histogram with customizations
ax = sns.histplot(temperatures, bins=15, kde=False, color='#3498db', binwidth=0.5)

# Customize the axes labels and the chart title
ax.set_title('Distribution of Daily Maximum Temperatures', fontsize=16)
ax.set_xlabel('Temperature (Celsius)', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

# Finalize and display the plot
plt.tight_layout()
plt.show()