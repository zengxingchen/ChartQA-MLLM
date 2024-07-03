
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Genre': 'Mystery', 'Circulation(%)': 16},
    {'Genre': 'Science Fiction', 'Circulation(%)': 11},
    {'Genre': 'Romance', 'Circulation(%)': 14},
    {'Genre': 'Biography', 'Circulation(%)': 9},
    {'Genre': "Children's Literature", 'Circulation(%)': 13},
    {'Genre': 'Self-help', 'Circulation(%)': 7},
    {'Genre': 'History', 'Circulation(%)': 8},
    {'Genre': 'Fantasy', 'Circulation(%)': 12},
    {'Genre': 'Graphic Novels', 'Circulation(%)': 5},
    {'Genre': 'Educational', 'Circulation(%)': 2},
    {'Genre': 'Poetry', 'Circulation(%)': 1},
    {'Genre': 'Other', 'Circulation(%)': 2}
]

# Prepare the data for the pie chart
labels = [entry['Genre'] for entry in data]
sizes = [entry['Circulation(%)'] for entry in data]

# Create the pie chart
plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart
plt.title('Book Genre Circulation')
plt.show()