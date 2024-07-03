
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = [
    {'Beverage Type': 'Espresso', 'Units Sold': 120},
    {'Beverage Type': 'Cappuccino', 'Units Sold': 85},
    {'Beverage Type': 'Latte', 'Units Sold': 140},
    {'Beverage Type': 'American Coffee', 'Units Sold': 75},
    {'Beverage Type': 'Mocha', 'Units Sold': 60}
]

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Initialize a seaborn style
sns.set_theme(style="whitegrid")

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(8, 6))

# Create a color palette
palette = sns.color_palette("husl", 5)

# Create a barplot
sns.barplot(
    x='Beverage Type', 
    y='Units Sold', 
    data=df, 
    palette=palette, 
    ax=ax
)

# Add title and labels to the chart
ax.set_title('Units Sold by Beverage Type', fontsize=16)
ax.set_xlabel('Beverage Type', fontsize=12)
ax.set_ylabel('Units Sold', fontsize=12)

# Show the value on top of each bar for clarity
for index, row in df.iterrows():
    ax.text(index, row['Units Sold'], row['Units Sold'], color='black', ha="center")

# Show the plot
plt.xticks(rotation=45) # Rotate x-axis labels for better readability
plt.tight_layout() # To ensure nothing is cut off
plt.show()