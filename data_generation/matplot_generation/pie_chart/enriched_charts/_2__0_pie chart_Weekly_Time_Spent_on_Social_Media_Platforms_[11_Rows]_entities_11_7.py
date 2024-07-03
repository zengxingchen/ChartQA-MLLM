
import matplotlib.pyplot as plt

# Data
fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew']
market_share = [30, 25, 15, 10, 8, 7, 5, 3]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#C71585', '#8A2BE2', '#FF6347']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 7))  # Change width and height
ax.pie(market_share, labels=fruits, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Setting the title
plt.title("Fruit Market Share in Local Market - 2023", pad=20)

# Display the chart
plt.show()