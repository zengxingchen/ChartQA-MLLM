
import matplotlib.pyplot as plt

# Data to plot
labels = 'E-commerce', 'Fintech', 'Healthcare', 'SaaS', 'Blockchain'
sizes = [35, 25, 20, 10, 10]
colors = ['#ff6347', '#4682b4', '#dda0dd', '#32cd32', '#ff8c00']

# Change the size of the figure (width, height)
plt.figure(figsize=(12, 8))

# Plot
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Market Share of Emerging Business Sectors', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()