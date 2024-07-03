
import matplotlib.pyplot as plt

# Data to plot
labels = ['Fruits', 'Vegetables', 'Grains', 'Proteins', 'Dairy']
sizes = [35.5, 30.2, 20.8, 10.3, 3.2]
colors = ['#ffcc00', '#66ff66', '#ff6666', '#66b3ff', '#cc99ff']

# Create pie chart
plt.figure(figsize=(12, 10))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Food Groups in a Balanced Diet', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()