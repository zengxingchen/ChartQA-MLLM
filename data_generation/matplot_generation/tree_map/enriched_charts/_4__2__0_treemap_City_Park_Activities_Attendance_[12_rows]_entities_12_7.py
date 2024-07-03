
import matplotlib.pyplot as plt
import squarify

# Data points
sports = ['Soccer', 'Basketball', 'Baseball', 'Tennis', 'Golf', 'American Football', 'Cricket', 
          'Rugby', 'Boxing', 'Formula 1', 'Cycling', 'Athletics', 'Swimming', 'MMA', 'Esports']
values = [7800, 6200, 5400, 4800, 4200, 3800, 3500, 3200, 2900, 2600, 2300, 2000, 1800, 1600, 1400]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A5', '#FF8C33', '#33FFF4', '#FF33D1', 
          '#FF3333', '#33FFCE', '#FF9F33', '#57FF33', '#FF3357', '#33A5FF', '#A533FF', '#8CFF33']

# Plot Dimensions
plt.figure(figsize=(16, 12))

# Create a treemap
squarify.plot(sizes=values, label=sports, color=colors, alpha=0.8)

# Title
plt.title('Market Value of Various Sports (in Millions)', fontsize=20, y=1.02)

# Remove axes
plt.axis('off')

# Show plot
plt.show()