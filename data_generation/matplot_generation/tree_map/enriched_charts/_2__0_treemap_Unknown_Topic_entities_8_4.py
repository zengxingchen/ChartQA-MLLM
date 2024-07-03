
import matplotlib.pyplot as plt
import squarify

# Data
philosophers = ['Plato', 'Aristotle', 'Kant', 'Nietzsche', 'Socrates', 'Descartes', 'Hegel', 'Hume', 'Locke', 'Rousseau', 'Other']
influence_values = [25.0, 15.5, 12.8, 10.2, 8.6, 7.4, 6.3, 5.5, 4.6, 3.7, 2.4]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ffbb78']

# Create a figure with specified size
plt.figure(figsize=(12, 10))

# Create a treemap with the above data
squarify.plot(sizes=influence_values, label=philosophers, color=colors, alpha=0.8)

# Title of the treemap
plt.title('Influence of Prominent Philosophers', fontsize=20)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()