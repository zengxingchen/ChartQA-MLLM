
import matplotlib.pyplot as plt
import squarify

# Data for global energy consumption by source
energy_sources = ['Hydro', 'Solar', 'Wind', 'Nuclear', 'Coal', 'Natural Gas', 'Geothermal', 'Biomass']
percentages = [16.2, 8.7, 15.1, 10.6, 38.4, 19.8, 0.4, 0.8]

# Custom color scheme
colors = ['#4F97A3', '#FFD700', '#89CFF0', '#C390D4', '#333333', '#F67280', '#88AB75', '#FF9655']

# Treemap
plt.figure(figsize=(14, 10))  # Adjusting the size of the treemap for better clarity
squarify.plot(sizes=percentages, label=energy_sources, color=colors, alpha=0.7)
plt.title('Global Energy Consumption by Source in 2021',fontsize=20, pad=20)
plt.axis('off')  # No axes for a cleaner look

plt.show()