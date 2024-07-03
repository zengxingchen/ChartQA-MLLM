
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the provided data
data = [
    {'City': 'Amsterdam', 'Total Stations': 300, 'Total Bicycles': 3500, 'Average Daily Riders': 4500, 'Bubble Size (Average Trips per Bicycle)': 1.29},
    {'City': 'Copenhagen', 'Total Stations': 100, 'Total Bicycles': 1650, 'Average Daily Riders': 2600, 'Bubble Size (Average Trips per Bicycle)': 1.58},
    {'City': 'Paris', 'Total Stations': 1230, 'Total Bicycles': 14500, 'Average Daily Riders': 17000, 'Bubble Size (Average Trips per Bicycle)': 1.17},
    {'City': 'Montreal', 'Total Stations': 460, 'Total Bicycles': 5000, 'Average Daily Riders': 4000, 'Bubble Size (Average Trips per Bicycle)': 0.8},
    {'City': 'New York', 'Total Stations': 776, 'Total Bicycles': 12000, 'Average Daily Riders': 14000, 'Bubble Size (Average Trips per Bicycle)': 1.17}
]
df = pd.DataFrame(data)

# Scale the bubble sizes to make differences more visible
# You may want to adjust the scaling factor as needed for better visualization
bubble_scale = 100
df['Scaled Bubble Size'] = df['Bubble Size (Average Trips per Bicycle)'] * bubble_scale

# Use Seaborn to create the bubble chart
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
bubble_chart = sns.scatterplot(data=df,
                               x='Total Stations',
                               y='Total Bicycles',
                               size='Scaled Bubble Size',
                               sizes=(50, 500), # The range of bubble sizes
                               hue='City',      # Color by city
                               alpha=0.7,       # Transparency of the bubbles
                               legend='brief')  # Include legend (use 'full' for full legend)

# Additional customizations
plt.title('Bubble Chart of Bike Sharing Data')
plt.xlabel('Total Stations')
plt.ylabel('Total Bicycles')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.) # Position the legend

# Show plot with a tight layout
plt.tight_layout()
plt.show()