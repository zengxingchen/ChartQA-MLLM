
import matplotlib.pyplot as plt
import numpy as np

# Data
destinations = ['Paris', 'Tokyo', 'New York', 'Sydney', 'Rome', 'Cape Town', 'Rio de Janeiro', 'Dubai', 'Bangkok', 'Cairo']
hiking = np.array([10, 5, 8, 12, 15, 20, 10, 5, 8, 12])
swimming = np.array([15, 20, 10, 18, 12, 15, 25, 10, 15, 18])
sightseeing = np.array([40, 30, 35, 25, 30, 25, 20, 25, 20, 22])
food_tasting = np.array([20, 25, 22, 30, 18, 30, 30, 40, 32, 28])
shopping = np.array([15, 20, 25, 15, 25, 10, 15, 20, 25, 20])

# Stack data for percentage calculation
total = hiking + swimming + sightseeing + food_tasting + shopping
hiking_percentage = hiking / total * 100
swimming_percentage = swimming / total * 100
sightseeing_percentage = sightseeing / total * 100
food_tasting_percentage = food_tasting / total * 100
shopping_percentage = shopping / total * 100

# Plot
fig, ax = plt.subplots(figsize=(12, 7))
bar_width = 0.85

p1 = ax.barh(destinations, hiking_percentage, color='#FF5733', edgecolor='white', height=bar_width)
p2 = ax.barh(destinations, swimming_percentage, left=hiking_percentage, color='#33FF57', edgecolor='white', height=bar_width)
p3 = ax.barh(destinations, sightseeing_percentage, left=hiking_percentage + swimming_percentage, color='#3357FF', edgecolor='white', height=bar_width)
p4 = ax.barh(destinations, food_tasting_percentage, left=hiking_percentage + swimming_percentage + sightseeing_percentage, color='#FF33A1', edgecolor='white', height=bar_width)
p5 = ax.barh(destinations, shopping_percentage, left=hiking_percentage + swimming_percentage + sightseeing_percentage + food_tasting_percentage, color='#F3FF33', edgecolor='white', height=bar_width)

# Add labels and title
ax.set_xlabel('Percentage')
ax.set_title('Preferred Tourist Activities in Various Destinations')
ax.legend((p1[0], p2[0], p3[0], p4[0], p5[0]), ('Hiking', 'Swimming', 'Sightseeing', 'Food Tasting', 'Shopping'), loc='lower right')

# Show plot
plt.tight_layout()
plt.show()