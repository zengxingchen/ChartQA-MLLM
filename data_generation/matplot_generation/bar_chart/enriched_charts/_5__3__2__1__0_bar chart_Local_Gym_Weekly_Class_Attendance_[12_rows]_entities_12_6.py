
import matplotlib.pyplot as plt

# Data
cuisines = ['Italian', 'Chinese', 'Mexican', 'Indian', 'Japanese', 'Mediterranean', 'Thai', 'French', 
            'Greek', 'Spanish', 'Lebanese', 'Turkish', 'Vietnamese', 'Korean', 'Caribbean', 'Brazilian']
restaurants = [3400, 3200, 2800, 2600, 2400, 2200, 2000, 1800, 1600, 1400, 1200, 1000, 800, 600, 400, 200]

# Create horizontal bar chart
plt.figure(figsize=(14, 8))  # Change width and height of the chart
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', 
          '#FF4500', '#20B2AA', '#FF69B4', '#A52A2A', '#5F9EA0', 
          '#D2691E', '#7FFF00', '#8B4513', '#00FA9A', '#DA70D6', '#6495ED']

plt.barh(cuisines, restaurants, color=colors, height=0.6)  # Change direction of chart and bar width

# Customizing the plot
plt.xlabel('Number of Restaurants')
plt.title('Number of Restaurants by Type of Cuisine (2023)', pad=20)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.xlim(100, 3600)  # Truncate y-axis to start from 100

plt.tight_layout()
plt.show()