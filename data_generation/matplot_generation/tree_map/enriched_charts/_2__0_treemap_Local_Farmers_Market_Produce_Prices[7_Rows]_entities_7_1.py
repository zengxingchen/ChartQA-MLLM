
import matplotlib.pyplot as plt
import squarify

# Data points
destinations = ['Paris', 'Bangkok', 'London', 'Dubai', 'Singapore', 'New York City', 'Istanbul', 
                'Tokyo', 'Rome', 'Antalya', 'Phuket', 'Mecca', 'Seoul', 'Hong Kong', 'Barcelona', 
                'Osaka', 'Las Vegas', 'Amsterdam', 'Madrid', 'Prague', 'Vienna', 'Milan', 
                'Buenos Aires', 'San Francisco', 'Sydney', 'Rio de Janeiro', 'Cape Town', 
                'Toronto', 'Moscow', 'Others']
market_share = [8.3, 6.5, 6.0, 5.8, 5.5, 4.9, 4.6, 4.4, 4.1, 3.9, 3.7, 3.5, 3.2, 3.0, 2.8, 
                2.6, 2.4, 2.2, 2.1, 1.9, 1.8, 1.6, 1.4, 1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 10.3]

# Color scheme
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF5733', '#33FFF0', '#3377FF', 
          '#57FF33', '#A833FF', '#5733FF', '#33FF57', '#FF5733', '#5733FF', '#FF3357', 
          '#57FF33', '#33FF57', '#3357FF', '#FF5733', '#33FF57', '#5733FF', '#33FFF0', 
          '#3377FF', '#FF33A8', '#33FF57', '#A833FF', '#5733FF', '#FF5733', '#FF33A8', 
          '#33FF57', '#D3D3D3']

plt.figure(figsize=(14, 10))
squarify.plot(sizes=market_share, label=destinations, color=colors, alpha=0.7)

# Chart details
plt.title('Popular Travel Destinations and Their Market Share in 2023', fontsize=18, y=1.05)
plt.axis('off')

plt.show()