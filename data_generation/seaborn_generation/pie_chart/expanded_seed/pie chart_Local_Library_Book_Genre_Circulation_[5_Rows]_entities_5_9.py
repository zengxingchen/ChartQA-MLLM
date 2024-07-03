
import matplotlib.pyplot as plt

# Your table data
data = [
    {'Genre': 'Mystery', 'Checkout Count': 150},
    {'Genre': 'Science Fiction', 'Checkout Count': 120},
    {'Genre': 'Biographies', 'Checkout Count': 90},
    {'Genre': "Children's Books", 'Checkout Count': 200},
    {'Genre': 'Self-Help', 'Checkout Count': 40}
]

# Extracting data for the pie chart
genres = [item['Genre'] for item in data]
checkout_counts = [item['Checkout Count'] for item in data]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(checkout_counts, labels=genres, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
plt.title('Genre Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()