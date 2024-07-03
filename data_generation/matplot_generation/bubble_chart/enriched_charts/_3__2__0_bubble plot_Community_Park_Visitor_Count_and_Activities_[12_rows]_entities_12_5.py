
import matplotlib.pyplot as plt

# Data
cities = ['Central Park', 'Golden Gate Park', 'Hyde Park', 'Stanley Park', 'Chapultepec', 'Ueno Park', 'Tiergarten', 'Kings Park', 'Luxembourg Gardens', 'Vondelpark']
avg_annual_visitors = [42, 24, 13, 8.5, 19, 10, 6.5, 6, 9, 12]
park_area = [341, 411, 142, 405, 686, 133, 210, 400, 23, 47]
green_space_percentage = [30, 37, 23, 45, 51, 25, 43, 63, 20, 27]
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#5F9EA0', '#D2691E', '#DC143C', '#2E8B57', '#DAA520', '#4B0082', '#7FFF00']

# Bubble chart
plt.figure(figsize=(18, 14))
for idx, city in enumerate(cities):
    plt.scatter(avg_annual_visitors[idx], park_area[idx], s=green_space_percentage[idx]*30, c=colors[idx], label=city, alpha=0.7, edgecolors='w')

# Add titles and labels
plt.title('Popularity and Size of Urban Parks', fontsize=20, pad=20)
plt.xlabel('Average Annual Visitors (Millions)', fontsize=16)
plt.ylabel('Park Area (Hectares)', fontsize=16)

# Additional settings
plt.grid(True)
plt.legend(loc='lower left', title='Parks')
plt.xlim(5, 45)
plt.ylim(20, 700)

# Show plot
plt.tight_layout()
plt.show()