
import matplotlib.pyplot as plt

# Given chart table data
data = [
    {'Drink': 'Americano', 'Number of Orders': 120},
    {'Drink': 'Latte', 'Number of Orders': 350},
    {'Drink': 'Cappuccino', 'Number of Orders': 180},
    {'Drink': 'Espresso', 'Number of Orders': 90},
    {'Drink': 'Iced Coffee', 'Number of Orders': 230},
    {'Drink': 'Mocha', 'Number of Orders': 160},
    {'Drink': 'Tea', 'Number of Orders': 60},
    {'Drink': 'Hot Chocolate', 'Number of Orders': 45}
]

# Extracting drink names and the number of orders for the pie chart
labels = [entry['Drink'] for entry in data]
sizes = [entry['Number of Orders'] for entry in data]

# Define color palette for each slice of the pie chart
colors = [
    'gold', 'yellowgreen', 'lightcoral', 'lightskyblue',
    'purple', 'orange', 'pink', 'brown'
]

# Set up the pie chart with additional visual encodings
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)  # Only "explode" the 1st slice (Americano)

fig1, ax1 = plt.subplots()
ax1.pie(
    sizes, 
    explode=explode, 
    labels=labels, 
    colors=colors,
    autopct='%1.1f%%',   # Adding a percentage to each slice
    shadow=True, 
    startangle=90
)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax1.axis('equal')  

# Optional: Add a title to the figure
plt.title('Number of Orders per Drink')

# Display the pie chart
plt.show()