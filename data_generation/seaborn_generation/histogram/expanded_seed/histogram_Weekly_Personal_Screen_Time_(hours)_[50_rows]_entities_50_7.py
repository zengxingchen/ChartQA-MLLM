
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Your provided data
data = [
    {'Week': 1, 'Screen Time (hours)': 21}, {'Week': 2, 'Screen Time (hours)': 35},
    {'Week': 3, 'Screen Time (hours)': 28}, {'Week': 4, 'Screen Time (hours)': 42},
    {'Week': 5, 'Screen Time (hours)': 31}, {'Week': 6, 'Screen Time (hours)': 26},
    {'Week': 7, 'Screen Time (hours)': 37}, {'Week': 8, 'Screen Time (hours)': 40},
    {'Week': 9, 'Screen Time (hours)': 23}, {'Week': 10, 'Screen Time (hours)': 33},
    {'Week': 11, 'Screen Time (hours)': 29}, {'Week': 12, 'Screen Time (hours)': 41},
    {'Week': 13, 'Screen Time (hours)': 39}, {'Week': 14, 'Screen Time (hours)': 22},
    {'Week': 15, 'Screen Time (hours)': 30}
]

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Increase the figure size
plt.figure(figsize=(10, 6))

# Create a histogram with additional visual encoding
# such as different color, edgecolor and a density plot on top of the histogram.
sns.histplot(
    data=df, 
    x='Screen Time (hours)', 
    bins=10,  # You can change the number of bins for granularity
    kde=True,  # Add a density plot
    color='skyblue',  # Change the fill color of the bars
    edgecolor='black',  # Color for the edges of the bars
    linewidth=1.5  # Width of the lines at the edges of the bars
)

# Customize the title and axis labels
plt.title('Distribution of Weekly Screen Time (hours)', fontsize=16)
plt.xlabel('Screen Time (hours)', fontsize=14)
plt.ylabel('Count', fontsize=14)

# Show the plot
plt.show()