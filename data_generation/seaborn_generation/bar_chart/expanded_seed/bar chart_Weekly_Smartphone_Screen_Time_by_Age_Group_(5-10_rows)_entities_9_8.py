
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given chart data
data = [
    {'Age Group': '16-20', 'Screen Time (Hours)': 21},
    {'Age Group': '21-25', 'Screen Time (Hours)': 18},
    {'Age Group': '26-30', 'Screen Time (Hours)': 16},
    {'Age Group': '31-35', 'Screen Time (Hours)': 14},
    {'Age Group': '36-40', 'Screen Time (Hours)': 12},
    {'Age Group': '41-45', 'Screen Time (Hours)': 10},
    {'Age Group': '46-50', 'Screen Time (Hours)': 8},
    {'Age Group': '51-55', 'Screen Time (Hours)': 6},
    {'Age Group': '56-60', 'Screen Time (Hours)': 4}
]

# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(data)

# Plotting the bar chart using seaborn
plt.figure(figsize=(10, 6))  # Set the figure size
sns.set_style('whitegrid')   # Set the style of the plot

# Create the barplot
barplot = sns.barplot(
    x='Age Group',
    y='Screen Time (Hours)',
    data=df,
    palette='viridis',  # Set the color palette
    edgecolor='black',  # Set the color of the bar edges
)

# Set the title and labels of the plot
plt.title('Average Screen Time per Age Group', fontsize=16)
plt.xlabel('Age Group', fontsize=14)
plt.ylabel('Average Screen Time (Hours)', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.show()