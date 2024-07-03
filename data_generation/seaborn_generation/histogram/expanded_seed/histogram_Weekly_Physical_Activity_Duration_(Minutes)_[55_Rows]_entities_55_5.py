
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data preparation
data_points = [
    {'Weekly Exercise (Minutes)': 450}, {'Weekly Exercise (Minutes)': 60},
    {'Weekly Exercise (Minutes)': 300}, {'Weekly Exercise (Minutes)': 210},
    {'Weekly Exercise (Minutes)': 400}, {'Weekly Exercise (Minutes)': 30},
    {'Weekly Exercise (Minutes)': 500}, {'Weekly Exercise (Minutes)': 240},
    {'Weekly Exercise (Minutes)': 180}, {'Weekly Exercise (Minutes)': 360},
    {'Weekly Exercise (Minutes)': 80}, {'Weekly Exercise (Minutes)': 120},
    {'Weekly Exercise (Minutes)': 310}, {'Weekly Exercise (Minutes)': 275},
    {'Weekly Exercise (Minutes)': 350}
]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data_points)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Creating the histogram using seaborn
plt.figure(figsize=(10, 6))
sns.histplot(
    df['Weekly Exercise (Minutes)'],
    bins=8,  # Assuming 8 bins for the histogram
    kde=False,  # Disabling the kernel density estimate
    color='skyblue',  # Choosing a color for the bars
    edgecolor='black',  # Edge color for bars for better definition
    linewidth=1.2  # Line width for edge color
)

# Further customization for a diversified visual encoding
plt.title('Histogram of Weekly Exercise (Minutes)', fontsize=16)
plt.xlabel('Weekly Exercise (Minutes)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Adding vertical lines for mean and median
mean_value = df['Weekly Exercise (Minutes)'].mean()
median_value = df['Weekly Exercise (Minutes)'].median()
plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_value:.2f}')
plt.axvline(median_value, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median_value:.2f}')

plt.legend()

# Show plot
plt.show()