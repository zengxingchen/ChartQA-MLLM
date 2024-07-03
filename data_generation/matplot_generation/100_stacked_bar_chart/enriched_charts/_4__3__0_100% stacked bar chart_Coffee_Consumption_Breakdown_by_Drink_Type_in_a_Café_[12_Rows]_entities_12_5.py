
import matplotlib.pyplot as plt
import numpy as np

# Data
destinations = ['Paris', 'Tokyo', 'New York', 'Sydney', 'Rome', 'Cape Town', 'Rio de Janeiro', 'Dubai', 'Bangkok', 'Cairo']
hiking = np.array([12, 8, 10, 14, 12, 18, 10, 6, 12, 14])
swimming = np.array([18, 25, 20, 16, 18, 22, 28, 18, 22, 20])
sightseeing = np.array([42, 28, 35, 30, 33, 25, 22, 30, 25, 28])
food_tasting = np.array([15, 25, 22, 24, 20, 20, 30, 32, 28, 22])
shopping = np.array([13, 14, 13, 16, 17, 15, 10, 14, 13, 16])

# Stack data for percentage calculation
total = hiking + swimming + sightseeing + food_tasting + shopping
hiking_percentage = hiking / total * 100
swimming_percentage = swimming / total * 100
sightseeing_percentage = sightseeing / total * 100
food_tasting_percentage = food_tasting / total * 100
shopping_percentage = shopping / total * 100

# Plot
fig, ax = plt.subplots(figsize=(10, 8))
bar_width = 0.65

p1 = ax.bar(destinations, hiking_percentage, color='#FF5733', edgecolor='white', width=bar_width)
p2 = ax.bar(destinations, swimming_percentage, bottom=hiking_percentage, color='#33FF57', edgecolor='white', width=bar_width)
p3 = ax.bar(destinations, sightseeing_percentage, bottom=hiking_percentage + swimming_percentage, color='#3357FF', edgecolor='white', width=bar_width)
p4 = ax.bar(destinations, food_tasting_percentage, bottom=hiking_percentage + swimming_percentage + sightseeing_percentage, color='#FF33A1', edgecolor='white', width=bar_width)
p5 = ax.bar(destinations, shopping_percentage, bottom=hiking_percentage + swimming_percentage + sightseeing_percentage + food_tasting_percentage, color='#F3FF33', edgecolor='white', width=bar_width)

# Add labels and title
ax.set_ylabel('Percentage')
ax.set_title('Preferred Tourist Activities in Various Destinations', pad=20)
ax.legend((p1[0], p2[0], p3[0], p4[0], p5[0]), ('Hiking', 'Swimming', 'Sightseeing', 'Food Tasting', 'Shopping'), loc='upper right')

# Show plot
plt.tight_layout()
plt.show()