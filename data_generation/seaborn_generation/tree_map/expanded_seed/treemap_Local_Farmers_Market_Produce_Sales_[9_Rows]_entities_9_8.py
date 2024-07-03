
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Our chart table data
chart_data = [
    {'Type': 'Fruit', 'Fruit/Vegetable': 'Apples', 'Total Sales (Units)': 1500, 'Average Price per Unit (USD)': 0.75, 'Season': 'Autumn'},
    {'Type': 'Fruit', 'Fruit/Vegetable': 'Oranges', 'Total Sales (Units)': 1200, 'Average Price per Unit (USD)': 0.5, 'Season': 'Winter'},
    {'Type': 'Vegetable', 'Fruit/Vegetable': 'Carrots', 'Total Sales (Units)': 800, 'Average Price per Unit (USD)': 0.3, 'Season': 'Spring'},
    {'Type': 'Vegetable', 'Fruit/Vegetable': 'Tomatoes', 'Total Sales (Units)': 1800, 'Average Price per Unit (USD)': 0.9, 'Season': 'Summer'},
    {'Type': 'Vegetable', 'Fruit/Vegetable': 'Broccoli', 'Total Sales (Units)': 600, 'Average Price per Unit (USD)': 1.25, 'Season': 'Fall'},
    {'Type': 'Fruit', 'Fruit/Vegetable': 'Bananas', 'Total Sales (Units)': 1300, 'Average Price per Unit (USD)': 0.45, 'Season': 'All Year'},
    {'Type': 'Fruit', 'Fruit/Vegetable': 'Peaches', 'Total Sales (Units)': 950, 'Average Price per Unit (USD)': 1.0, 'Season': 'Summer'},
    {'Type': 'Vegetable', 'Fruit/Vegetable': 'Spinach', 'Total Sales (Units)': 700, 'Average Price per Unit (USD)': 0.9, 'Season': 'Spring'},
    {'Type': 'Fruit', 'Fruit/Vegetable': 'Strawberries', 'Total Sales (Units)': 1100, 'Average Price per Unit (USD)': 1.2, 'Season': 'Spring'}
]

# Converting the list of dictionaries into a pandas DataFrame
data = pd.DataFrame(chart_data)

# Creating a treemap
plt.figure(figsize=(12, 8))

# Colors for different types of produce
colors = {
    'Fruit': 'skyblue',
    'Vegetable': 'lightgreen'
}

# Mapping the colors based on the 'Type' column of the DataFrame
data['color'] = data['Type'].map(colors)

# Using the squarify library to plot the treemap
squarify.plot(sizes=data['Total Sales (Units)'],
              label=data['Fruit/Vegetable'],
              color=data['color'],
              alpha=0.8,
              text_kwargs={'fontsize':9})

plt.title('Sales Units Breakdown by Fruit/Vegetable')
plt.axis('off')  # Turn off the axis

# Legend
for t in colors:
    plt.scatter([], [], color=colors[t], label=t)

plt.legend(title='Type', frameon=False, bbox_to_anchor=(1, 1), loc='upper left')
plt.show()