
import matplotlib.pyplot as plt

# Data to plot
labels = 'Sun', 'Planets', 'Asteroids', 'Comets', 'Moons', 'Other'
sizes = [99.8, 0.2, 0.05, 0.03, 0.02, 0.005]
colors = ['#ff4500','#4682b4','#ffd700','#32cd32','#ff69b4','#8a2be2']

# Change the size of the figure (width, height)
plt.figure(figsize=(14, 10))

# Plot
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Composition of the Solar System', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()