
import matplotlib.pyplot as plt

# Your provided data
data = [
    {'MenuItem': 'Espresso', 'Sales Percentage': 18.0},
    {'MenuItem': 'Latte', 'Sales Percentage': 24.0},
    {'MenuItem': 'Cappuccino', 'Sales Percentage': 13.0},
    {'MenuItem': 'Americano', 'Sales Percentage': 9.0},
    {'MenuItem': 'Mocha', 'Sales Percentage': 10.0},
    {'MenuItem': 'Hot Chocolate', 'Sales Percentage': 6.0},
    {'MenuItem': 'Tea', 'Sales Percentage': 4.0},
    {'MenuItem': 'Iced Coffee Drinks', 'Sales Percentage': 12.0},
    {'MenuItem': 'Pastries', 'Sales Percentage': 2.0},
    {'MenuItem': 'Sandwiches', 'Sales Percentage': 1.0},
    {'MenuItem': 'Salads', 'Sales Percentage': 0.5},
    {'MenuItem': 'Others', 'Sales Percentage': 0.5}
]

# Preparing data for pie chart
labels = [item['MenuItem'] for item in data]
sizes = [item['Sales Percentage'] for item in data]

# Define exploding the slices (i.e. 'pop out' the first slice)
explode = [0.1 if i == labels.index('Latte') else 0 for i in range(len(labels))]

# Define colors for each slice
colors = plt.cm.Paired(range(len(labels)))

# Plotting the pie chart
plt.figure(figsize=(10, 8))  # Set the figure size
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Coffee Shop Sales Distribution')
plt.show()