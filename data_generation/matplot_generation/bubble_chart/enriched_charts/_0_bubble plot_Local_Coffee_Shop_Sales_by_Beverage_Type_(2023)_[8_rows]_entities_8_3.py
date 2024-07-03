
import matplotlib.pyplot as plt

# Data
countries = ['China', 'United States', 'India', 'Russia', 'Japan', 'Germany', 'Canada', 'Brazil', 'South Korea', 'Australia']
co2_emissions = [9040, 5000, 2060, 1460, 1060, 700, 550, 450, 640, 420]  # in million tonnes
forest_area = [22.3, 33.1, 24.1, 49.4, 68.5, 32.7, 38.2, 59.1, 63.3, 16.2]  # percentage of land area
population = [1395000, 331000, 1380000, 144500, 126500, 83200, 38000, 212500, 51200, 25600]  # in thousands

# Normalize the population data to use as bubble sizes
max_population = max(population)
bubble_sizes = [(p / max_population) * 1000 for p in population]

# Plot
plt.figure(figsize=(14, 7))  # Adjusted width and height of the chart
plt.scatter(co2_emissions, forest_area, s=bubble_sizes,
            color=['#FF6347', '#4682B4', '#FFD700', '#ADFF2F', '#6A5ACD', '#20B2AA', '#FF69B4', '#8B4513', '#708090', '#FFA500'],
            alpha=0.5)

# Additional Customization
plt.title('CO2 Emissions vs. Forest Area by Country')
plt.xlabel('CO2 Emissions (million tonnes)')
plt.ylabel('Forest Area (% of land area)')
plt.xticks(rotation=45)
plt.grid(True)

# Annotating the country names
for i, country in enumerate(countries):
    plt.text(co2_emissions[i], forest_area[i], country, ha='center', va='center')

# Show the plot
plt.tight_layout()
plt.show()