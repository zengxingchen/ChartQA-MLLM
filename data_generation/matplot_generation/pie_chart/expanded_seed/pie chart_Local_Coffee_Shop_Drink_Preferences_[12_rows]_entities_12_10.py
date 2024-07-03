
import matplotlib.pyplot as plt

# Data
data = [
    {'Drink Type': 'Espresso', 'Orders Per Day': 90},
    {'Drink Type': 'Americano', 'Orders Per Day': 140},
    {'Drink Type': 'Latte', 'Orders Per Day': 200},
    {'Drink Type': 'Cappuccino', 'Orders Per Day': 120},
    {'Drink Type': 'Mocha', 'Orders Per Day': 110},
    {'Drink Type': 'Flat White', 'Orders Per Day': 70},
    {'Drink Type': 'Iced Coffee', 'Orders Per Day': 150},
    {'Drink Type': 'Cold Brew', 'Orders Per Day': 100},
    {'Drink Type': 'Frappuccino', 'Orders Per Day': 80},
    {'Drink Type': 'Tea', 'Orders Per Day': 60},
    {'Drink Type': 'Hot Chocolate', 'Orders Per Day': 50},
    {'Drink Type': 'Herbal Tea', 'Orders Per Day': 30}
]

# Extracting the data
labels = [item['Drink Type'] for item in data]
sizes = [item['Orders Per Day'] for item in data]

# Colors for each section
colors = plt.cm.tab20c.colors  # using the tab20c colormap for a diverse set of colors

# Explode the 3 slices with the most orders
explode = [0.1 if item in sorted(sizes, reverse=True)[:3] else 0 for item in sizes]

# Pie chart
plt.figure(figsize=(10, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, shadow=True)

# Draw a circle in the center to turn the pie into a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Adding a title
plt.title('Daily Orders by Drink Type')

# Add a legend if required or preferred
plt.legend(labels, title="Drink Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Display the plot
plt.show()