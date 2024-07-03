
import matplotlib.pyplot as plt

# Given chart table data
data = [
    {'Device': 'Smartphones', 'Percentage': 48},
    {'Device': 'Laptops', 'Percentage': 26},
    {'Device': 'Desktops', 'Percentage': 17},
    {'Device': 'Tablets', 'Percentage': 5},
    {'Device': 'Smart TVs', 'Percentage': 4}
]

# Extracting the device names and percentages
devices = [item['Device'] for item in data]
percentages = [item['Percentage'] for item in data]

# Creating the pie chart
plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=devices, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)

# Adding a chart title
plt.title('Device Usage Distribution')

# Optional: Adding a legend
plt.legend(devices, title="Devices", loc="best")

# Show the plot
plt.show()