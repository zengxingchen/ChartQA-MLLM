
import matplotlib.pyplot as plt

# Data to plot
labels = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Mystery', 'Romance', 'Biography', 'History']
sizes = [25, 30, 15, 10, 8, 6, 4, 2]
colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', '#edc949', '#af7aa1', '#ff9da7']

# Plot
plt.figure(figsize=[10, 6])  # Set the width and height of the chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Book Genre Distribution', pad=20)
plt.show()