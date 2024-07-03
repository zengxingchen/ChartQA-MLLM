
import matplotlib.pyplot as plt

# Data to plot
labels = 'Beach Vacation', 'City Tour', 'Mountain Hiking', 'Cruise', 'Safari'
sizes = [35.0, 25.0, 20.0, 10.0, 10.0]
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# Create pie chart
plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Popularity of Vacation Activities in 2023', y=1.05)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()