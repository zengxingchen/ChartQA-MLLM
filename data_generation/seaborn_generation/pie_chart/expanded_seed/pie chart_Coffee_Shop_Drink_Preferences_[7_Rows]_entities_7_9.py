
import matplotlib.pyplot as plt

# Given data
data = [
    {'Drink Type': 'Espresso', 'Orders per Day': 75},
    {'Drink Type': 'Latte', 'Orders per Day': 150},
    {'Drink Type': 'Cappuccino', 'Orders per Day': 100},
    {'Drink Type': 'Iced Coffee', 'Orders per Day': 50},
    {'Drink Type': 'Macchiato', 'Orders per Day': 30},
    {'Drink Type': 'American', 'Orders per Day': 45},
    {'Drink Type': 'Tea', 'Orders per Day': 25}
]

# Extract the 'Drink Type' and 'Orders per Day' as separate lists
labels = [item['Drink Type'] for item in data]
sizes = [item['Orders per Day'] for item in data]

# Define colors
colors = plt.cm.Paired(range(len(data)))

# Create the pie chart
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

# Display the title
plt.title('Daily Orders per Drink Type')

# Show the chart
plt.show()