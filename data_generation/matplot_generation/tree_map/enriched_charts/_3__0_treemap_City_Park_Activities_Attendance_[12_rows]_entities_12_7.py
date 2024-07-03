
import matplotlib.pyplot as plt
import squarify

# Data points
platforms = ['Netflix', 'Amazon Prime Video', 'Disney+', 'Hulu', 'HBO Max', 'Paramount+', 
             'Apple TV+', 'Peacock', 'Discovery+', 'ESPN+', 'Showtime', 'Starz', 
             'Crunchyroll', 'BBC iPlayer', 'Sling TV']
subscribers_in_millions = [230, 175, 164, 48, 76, 60, 40, 28, 22, 24, 27, 26, 10, 9, 2.3]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#FF8C33', '#33FFF3', 
          '#5733FF', '#FF5733', '#57FF33', '#FF3357', '#33FF8C', '#8C33FF', '#3357A1', '#A1FF33']

# Plot Dimensions
plt.figure(figsize=(14, 10))

# Create a treemap
squarify.plot(sizes=subscribers_in_millions, label=platforms, color=colors, alpha=0.8)

# Title
plt.title('Subscribers of Streaming Services (in Millions)', fontsize=20)

# Remove axes
plt.axis('off')

# Show plot
plt.show()