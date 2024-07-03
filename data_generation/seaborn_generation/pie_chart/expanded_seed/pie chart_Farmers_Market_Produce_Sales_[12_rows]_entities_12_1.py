
import matplotlib.pyplot as plt

# Given data
chart_data = [
    {'Produce': 'Apples', 'Sales (in units)': 150},
    {'Produce': 'Oranges', 'Sales (in units)': 120},
    {'Produce': 'Bananas', 'Sales (in units)': 90},
    {'Produce': 'Strawberries', 'Sales (in units)': 110},
    {'Produce': 'Grapes', 'Sales (in units)': 80},
    {'Produce': 'Tomatoes', 'Sales (in units)': 140},
    {'Produce': 'Cucumbers', 'Sales (in units)': 70},
    {'Produce': 'Peppers', 'Sales (in units)': 60},
    {'Produce': 'Lettuce', 'Sales (in units)': 130},
    {'Produce': 'Carrots', 'Sales (in units)': 50},
    {'Produce': 'Blueberries', 'Sales (in units)': 40},
    {'Produce': 'Peaches', 'Sales (in units)': 30}
]

# Extracting data for plotting
labels = [item['Produce'] for item in chart_data]
sizes = [item['Sales (in units)'] for item in chart_data]

# Plotting the pie chart
plt.figure(figsize=(10, 8))  # Set the figure size
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the plot
plt.show()