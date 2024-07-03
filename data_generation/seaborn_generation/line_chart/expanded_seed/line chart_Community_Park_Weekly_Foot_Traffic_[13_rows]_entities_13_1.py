
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given dataset in a list of dictionaries format
data = [
    {'Week': 1, 'Joggers': 120, 'Parents with Strollers': 80, 'Dog Walkers': 95, 'Picnic Groups': 30, 'Bird Watchers': 10},
    {'Week': 2, 'Joggers': 132, 'Parents with Strollers': 85, 'Dog Walkers': 105, 'Picnic Groups': 35, 'Bird Watchers': 14},
    # ... include all other data points ...
    {'Week': 13, 'Joggers': 175, 'Parents with Strollers': 120, 'Dog Walkers': 145, 'Picnic Groups': 80, 'Bird Watchers': 35}
]

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(data)

# Set the style of the axes and the grid
sns.set_style('whitegrid')

# Create a lineplot for each column except 'Week'
palette = sns.color_palette("husl", 5)  # A palette with 5 distinguishable colors

plt.figure(figsize=(14, 8))  # Set the figure size

# Iterate over the columns to create a line for each type of park visitor
for i, visitor in enumerate(df.columns[1:]):
    sns.lineplot(
        x='Week', 
        y=visitor, 
        data=df, 
        marker='o',  # Each data point will be marked by a circle
        label=visitor,  # Label for the legend
        color=palette[i],  # Color from the palette
        linewidth=2.5,  # Width of the line
        linestyle='-'  # Solid line style
    )

# Set the title of the plot
plt.title('Park Visitors Over 13 Weeks', fontsize=16)

# Set the x and y axes labels
plt.xlabel('Week', fontsize=12)
plt.ylabel('Number of Visitors', fontsize=12)

# Increase the readability of x and y ticks
plt.xticks(range(1, 14), fontsize=10)
plt.yticks(fontsize=10)

# Display the legend
plt.legend(title='Visitor Types')

# Show the plot
plt.show()