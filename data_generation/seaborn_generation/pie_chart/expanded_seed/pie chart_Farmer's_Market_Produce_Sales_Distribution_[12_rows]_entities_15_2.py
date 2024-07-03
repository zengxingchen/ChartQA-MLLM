
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Produce Type': 'Apples', 'Percentage of Total Sales': '15%'},
    {'Produce Type': 'Tomatoes', 'Percentage of Total Sales': '12%'},
    {'Produce Type': 'Sweet Corn', 'Percentage of Total Sales': '10%'},
    {'Produce Type': 'Peaches', 'Percentage of Total Sales': '8%'},
    {'Produce Type': 'Strawberries', 'Percentage of Total Sales': '8%'},
    {'Produce Type': 'Green Beans', 'Percentage of Total Sales': '7%'},
    {'Produce Type': 'Blueberries', 'Percentage of Total Sales': '7%'},
    {'Produce Type': 'Watermelons', 'Percentage of Total Sales': '6%'},
    {'Produce Type': 'Lettuces', 'Percentage of Total Sales': '6%'},
    {'Produce Type': 'Carrots', 'Percentage of Total Sales': '5%'},
    {'Produce Type': 'Peppers', 'Percentage of Total Sales': '4%'},
    {'Produce Type': 'Herbs', 'Percentage of Total Sales': '3%'},
    {'Produce Type': 'Potatoes', 'Percentage of Total Sales': '3%'},
    {'Produce Type': 'Cucumbers', 'Percentage of Total Sales': '3%'},
    {'Produce Type': 'Onions', 'Percentage of Total Sales': '3%'}
]

# Extracting labels and sizes for the pie chart
labels = [item['Produce Type'] for item in data]
sizes = [int(item['Percentage of Total Sales'].rstrip('%')) for item in data]

# Colors can be specified for each slice if desired
colors = plt.cm.Paired(range(len(labels)))

# Explode the 1st slice (i.e., 'Apples')
explode = [0.1 if i == 0 else 0 for i in range(len(labels))]

# Plotting the pie chart
plt.figure(figsize=(10, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.

# Title for the pie chart
plt.title('Percentage of Total Sales by Produce Type')

# Display the pie chart
plt.show()