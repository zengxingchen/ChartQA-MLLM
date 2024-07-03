
import matplotlib.pyplot as plt
import squarify

# Dataset
countries = [
    'Finland', 'Norway', 'Iceland', 'Denmark', 'Netherlands', 'Sweden', 
    'Switzerland', 'Belgium', 'Luxembourg', 'Canada', 'Bosnia and Herzegovina',
    'Austria', 'Italy', 'Brazil', 'Slovenia', 'Germany', 'France'
]
consumption = [
    12.0, 9.9, 9.0, 8.7, 8.4, 8.2, 7.9, 6.8, 6.5, 6.2, 6.1, 6.0, 5.9, 5.8, 5.8, 5.5, 5.4
]

# Color Scheme
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33D4', '#D4FF33', '#5710FF', '#FFD433',
    '#D633FF', '#33FFD4', '#571033', '#5733FF', '#33D4FF', '#57FF33', '#FF5733',
    '#33FF57', '#3357FF', '#FFD433'
]

plt.figure(figsize=(14, 10))

# Creating the treemap
squarify.plot(sizes=consumption, label=countries, color=colors, alpha=0.8)

# Adding a title
plt.title('Global Coffee Consumption by Country (kg/person/year)', fontsize=16, weight='bold', y=1.05)

# Removing the axes
plt.axis('off')

# Display the plot
plt.show()