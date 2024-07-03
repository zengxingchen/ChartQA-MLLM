
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Convert the chart table data to a DataFrame.
data = pd.DataFrame([
    {'Month': 'January', 'Precipitation': 78},
    {'Month': 'February', 'Precipitation': 72},
    {'Month': 'March', 'Precipitation': 80},
    {'Month': 'April', 'Precipitation': 75},
    {'Month': 'May', 'Precipitation': 70},
    {'Month': 'June', 'Precipitation': 60},
    {'Month': 'July', 'Precipitation': 58},
    {'Month': 'August', 'Precipitation': 65},
    {'Month': 'September', 'Precipitation': 76},
    {'Month': 'October', 'Precipitation': 82},
    {'Month': 'November', 'Precipitation': 85},
    {'Month': 'December', 'Precipitation': 90}
])

# Convert 'Month' to a categorical type and order it correctly.
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                'August', 'September', 'October', 'November', 'December']
data['Month'] = pd.Categorical(data['Month'], categories=months_order, ordered=True)

# Create the line plot
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
line_plot = sns.lineplot(
    x='Month', 
    y='Precipitation', 
    data=data,
    marker='o',  # Add markers to each data point
    color="coral",  # Set the color of the line
    linewidth=2.5,  # Set the width of the line
    linestyle='--'  # Set the style of the line to dashed
)

# Add titles and labels
plt.title('Monthly Precipitation', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Precipitation (in millimeters)', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add grid lines for better readability
plt.grid(True)

# Show the plot
plt.show()