
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Temperature (°F)': 58, 'Iced Coffee Sales (Cups)': 30, 'Hot Coffee Sales (Cups)': 150},
    {'Temperature (°F)': 60, 'Iced Coffee Sales (Cups)': 40, 'Hot Coffee Sales (Cups)': 130},
    {'Temperature (°F)': 65, 'Iced Coffee Sales (Cups)': 60, 'Hot Coffee Sales (Cups)': 115},
    {'Temperature (°F)': 70, 'Iced Coffee Sales (Cups)': 120, 'Hot Coffee Sales (Cups)': 90},
    {'Temperature (°F)': 75, 'Iced Coffee Sales (Cups)': 200, 'Hot Coffee Sales (Cups)': 70},
    {'Temperature (°F)': 80, 'Iced Coffee Sales (Cups)': 250, 'Hot Coffee Sales (Cups)': 50},
    {'Temperature (°F)': 85, 'Iced Coffee Sales (Cups)': 270, 'Hot Coffee Sales (Cups)': 30},
    {'Temperature (°F)': 90, 'Iced Coffee Sales (Cups)': 300, 'Hot Coffee Sales (Cups)': 25},
    {'Temperature (°F)': 95, 'Iced Coffee Sales (Cups)': 320, 'Hot Coffee Sales (Cups)': 20},
    {'Temperature (°F)': 60, 'Iced Coffee Sales (Cups)': 45, 'Hot Coffee Sales (Cups)': 125},
    {'Temperature (°F)': 70, 'Iced Coffee Sales (Cups)': 110, 'Hot Coffee Sales (Cups)': 95},
    {'Temperature (°F)': 80, 'Iced Coffee Sales (Cups)': 240, 'Hot Coffee Sales (Cups)': 55}
]

# Create DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to make it work well with sns.scatterplot
df_melted = df.melt(id_vars='Temperature (°F)', var_name='Coffee Type', value_name='Sales (Cups)')

# Define a color palette for the coffee types
palette = {'Iced Coffee Sales (Cups)': 'blue', 'Hot Coffee Sales (Cups)': 'red'}

# Create the scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df_melted,
    x='Temperature (°F)',
    y='Sales (Cups)',
    hue='Coffee Type',  # Color by Coffee Type
    style='Coffee Type',  # Different markers by Coffee Type
    size='Sales (Cups)',  # Size by the number of sales
    sizes=(20, 200),  # Control the range of sizes
    palette=palette,  # Color palette defined above
)

# Customize the axes and title
plt.title('Coffee Sales vs Temperature')
plt.xlabel('Temperature (°F)')
plt.ylabel('Coffee Sales (Cups)')

# Add a legend to explain markers
plt.legend(title='Coffee Type and Sales', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()