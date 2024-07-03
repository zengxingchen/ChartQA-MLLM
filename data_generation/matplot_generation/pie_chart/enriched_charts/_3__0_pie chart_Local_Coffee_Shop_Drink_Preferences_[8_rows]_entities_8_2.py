
import matplotlib.pyplot as plt

# Data to plot
labels = 'Paintings', 'Sculptures', 'Installations', 'Photography', 'Digital Art', 'Prints', 'Drawings', 'Ceramics'
sizes = [220, 180, 90, 70, 50, 40, 30, 20]
colors = ['#ff6347', '#4682b4', '#32cd32', '#ff69b4', '#8a2be2', '#ffa500', '#00ced1', '#adff2f']

# Change the size of the figure (width, height)
plt.figure(figsize=(12, 7))

# Plot
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Art Forms in an Exhibition', y=1.08)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()