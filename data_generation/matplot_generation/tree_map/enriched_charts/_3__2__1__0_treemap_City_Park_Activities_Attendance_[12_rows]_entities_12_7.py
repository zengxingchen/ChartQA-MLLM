
import matplotlib.pyplot as plt
import squarify

# Data points
countries = ['India', 'Brazil', 'Australia', 'United States', 'Russia', 'China', 'Canada', 'South Africa', 'Indonesia', 
             'Peru', 'Kenya', 'Mexico', 'Thailand', 'Colombia', 'Tanzania', 'Malaysia', 'Argentina', 'Venezuela', 
             'Nepal', 'Vietnam', 'Uganda']
food_source_amount = [150, 140, 130, 120, 110, 105, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30]
colors = ['#ff5733', '#33ff57', '#3357ff', '#ff33a1', '#a133ff', '#33ffd4', '#ffae33', '#8b33ff', '#ff5733', 
          '#33ff57', '#3357ff', '#ff33a1', '#a133ff', '#33ffd4', '#ffae33', '#8b33ff', '#ff5733', '#33ff57', 
          '#3357ff', '#ff33a1', '#a133ff']

# Plot Dimensions
plt.figure(figsize=(18, 14))

# Create a treemap
squarify.plot(sizes=food_source_amount, label=countries, color=colors, alpha=0.8)

# Title
plt.title('Top Food and Nutrition Sources by Country', fontsize=22, pad=30)

# Remove axes
plt.axis('off')

# Show plot
plt.show()