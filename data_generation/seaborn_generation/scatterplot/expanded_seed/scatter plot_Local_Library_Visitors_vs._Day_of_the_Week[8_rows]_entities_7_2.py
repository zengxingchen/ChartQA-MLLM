
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = [
    {'Day of the Week': 'Monday', 'Number of Visitors': 75, 'Average Borrowed Books': 140},
    {'Day of the Week': 'Tuesday', 'Number of Visitors': 64, 'Average Borrowed Books': 125},
    {'Day of the Week': 'Wednesday', 'Number of Visitors': 58, 'Average Borrowed Books': 100},
    {'Day of the Week': 'Thursday', 'Number of Visitors': 80, 'Average Borrowed Books': 170},
    {'Day of the Week': 'Friday', 'Number of Visitors': 90, 'Average Borrowed Books': 200},
    {'Day of the Week': 'Saturday', 'Number of Visitors': 120, 'Average Borrowed Books': 310},
    {'Day of the Week': 'Sunday', 'Number of Visitors': 45, 'Average Borrowed Books': 70}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Now we prepare a scatterplot
sns.set_style("whitegrid") # You can change the grid style here, e.g., darkgrid, white, ticks, etc.

# Create a color palette
palette = sns.color_palette("husl", len(data))

# Create a scatterplot
plt.figure(figsize=(10, 6)) # You can modify the figure size as per your needs
scatter = sns.scatterplot(
    x='Number of Visitors', 
    y='Average Borrowed Books', 
    data=df, 
    hue='Day of the Week', # This encodes day of the week with different colors
    palette=palette, 
    s=100, # Adjusts the size of each point
    style='Day of the Week', # Different shapes for different days
    markers=True
)

# Customize the axes and labels
plt.title('Scatterplot of Library Visitors and Books Borrowed', fontsize=16)
plt.xlabel('Number of Visitors', fontsize=12)
plt.ylabel('Average Borrowed Books', fontsize=12)
scatter.legend(title='Day of the Week', bbox_to_anchor=(1.05, 1), loc='upper left') # Move the legend outside of the figure

# Show the plot
plt.tight_layout()
plt.show()