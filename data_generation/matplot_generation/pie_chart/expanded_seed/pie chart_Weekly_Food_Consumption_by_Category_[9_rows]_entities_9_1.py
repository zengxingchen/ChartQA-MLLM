
import matplotlib.pyplot as plt

# Provided chart table data
data = [
    {'Food Category': 'Vegetables', 'Percentage': 20},
    {'Food Category': 'Fruits', 'Percentage': 15},
    {'Food Category': 'Meat', 'Percentage': 25},
    {'Food Category': 'Dairy', 'Percentage': 10},
    {'Food Category': 'Grains', 'Percentage': 17},
    {'Food Category': 'Sweets', 'Percentage': 5},
    {'Food Category': 'Beverages', 'Percentage': 5},
    {'Food Category': 'Seafood', 'Percentage': 2},
    {'Food Category': 'Other Foods', 'Percentage': 1}
]

# Extracting the 'Food Category' and 'Percentage' data
categories = [item['Food Category'] for item in data]
percentages = [item['Percentage'] for item in data]

# Define colors for each pie slice
colors = [
    'lightgreen', 'orange', 'lightcoral', 'lightskyblue', 
    'yellowgreen', 'plum', 'lightpink', 'aqua', 'lightgrey'
]

# Explode the largest slice for emphasis (in this case 'Meat' at 25%)
explode = [0.1 if category == 'Meat' else 0 for category in categories]

# Create the pie chart
plt.figure(figsize=(10, 7))
plt.pie(percentages, labels=categories, explode=explode, colors=colors,
        autopct='%1.1f%%', startangle=140, shadow=True)

# Display the pie chart with title
plt.title('Food Categories Distribution')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

# Show the plot
plt.show()