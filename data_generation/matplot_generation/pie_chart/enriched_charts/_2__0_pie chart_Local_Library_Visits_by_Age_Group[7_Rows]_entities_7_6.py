
import matplotlib.pyplot as plt

# Data to plot
labels = ['Clothing', 'Accessories', 'Footwear', 'Beauty Products', 'Watches', 'Bags', 'Jewelry', 'Perfumes']
sizes = [30, 20, 15, 10, 5, 8, 7, 5]
colors = ['#FF7F50', '#6495ED', '#FFD700', '#FF6347', '#40E0D0', '#EE82EE', '#8A2BE2', '#A52A2A']

# Create pie chart
plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Popular Fashion & Beauty Categories', y=1.08)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()