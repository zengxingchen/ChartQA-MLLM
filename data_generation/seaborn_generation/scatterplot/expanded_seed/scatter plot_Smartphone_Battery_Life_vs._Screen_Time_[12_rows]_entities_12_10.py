
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data provided in table format
data = [
    {'User ID': 1, 'Battery Life (Hours)': 24, 'Average Screen Time (Hours/Day)': 3.5},
    {'User ID': 2, 'Battery Life (Hours)': 37, 'Average Screen Time (Hours/Day)': 2.1},
    {'User ID': 3, 'Battery Life (Hours)': 29, 'Average Screen Time (Hours/Day)': 4.2},
    {'User ID': 4, 'Battery Life (Hours)': 45, 'Average Screen Time (Hours/Day)': 1.8},
    {'User ID': 5, 'Battery Life (Hours)': 32, 'Average Screen Time (Hours/Day)': 5.0},
    {'User ID': 6, 'Battery Life (Hours)': 38, 'Average Screen Time (Hours/Day)': 2.6},
    {'User ID': 7, 'Battery Life (Hours)': 41, 'Average Screen Time (Hours/Day)': 1.9},
    {'User ID': 8, 'Battery Life (Hours)': 19, 'Average Screen Time (Hours/Day)': 6.8},
    {'User ID': 9, 'Battery Life (Hours)': 22, 'Average Screen Time (Hours/Day)': 4.6},
    {'User ID': 10, 'Battery Life (Hours)': 31, 'Average Screen Time (Hours/Day)': 3.8},
    {'User ID': 11, 'Battery Life (Hours)': 35, 'Average Screen Time (Hours/Day)': 2.0},
    {'User ID': 12, 'Battery Life (Hours)': 17, 'Average Screen Time (Hours/Day)': 7.1}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Create a scatter plot
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(
    x='Battery Life (Hours)',
    y='Average Screen Time (Hours/Day)',
    data=df,
    hue='User ID',  # Color code points by User ID for additional visual encoding
    palette='viridis',  # Color palette for diversity in hue
    size='Battery Life (Hours)',  # Vary the size of points based on battery life
    sizes=(40, 400),  # Control the range of sizes
    style='User ID',  # Different markers for each User ID
    markers=True,  # Use markers
    edgecolor='w',  # Add a white edge color to markers for better visibility
    legend='brief'  # Include a brief legend for hue, size and style
)

# Enhance the legend to span more than one column if needed
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Set titles and labels
plt.title('Scatter Plot of Battery Life vs. Average Screen Time')
plt.xlabel('Battery Life (Hours)')
plt.ylabel('Average Screen Time (Hours/Day)')

# Show the plot
plt.tight_layout()
plt.show()