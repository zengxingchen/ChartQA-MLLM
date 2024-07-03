
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Japan', 'Germany', 'India', 'Brazil', 'Canada', 'Russia', 'South Korea', 'Australia', 'United Kingdom', 'France', 'Italy', 'Mexico', 'Spain']
gdp_growth = [2.3, 6.1, 0.7, 1.5, 5.0, 1.1, 1.9, 1.3, 2.0, 2.2, 1.4, 1.3, 0.9, 2.1, 1.2]  # percentage
unemployment_rate = [3.7, 5.2, 2.4, 3.2, 7.4, 11.9, 5.5, 4.6, 3.6, 4.5, 4.0, 8.5, 9.8, 3.6, 13.8]  # percentage
population = [331000, 1395000, 126500, 83200, 1380000, 212500, 38000, 144500, 51200, 25600, 67800, 67000, 60500, 128900, 47300]  # in thousands

# Normalize the population data to use as bubble sizes
max_population = max(population)
bubble_sizes = [(p / max_population) * 1000 for p in population]

# Plot
plt.figure(figsize=(16, 9))  # Adjusted width and height of the chart
plt.scatter(gdp_growth, unemployment_rate, s=bubble_sizes,
            color=['#FF6347', '#4682B4', '#FFD700', '#ADFF2F', '#6A5ACD', '#20B2AA', '#FF69B4', '#8B4513', '#708090', '#FFA500', '#FF4500', '#2E8B57', '#D2691E', '#8A2BE2', '#A52A2A'],
            alpha=0.6)

# Additional Customization
plt.title('GDP Growth vs. Unemployment Rate by Country', pad=20)
plt.xlabel('GDP Growth (%)')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)

# Annotating the country names
for i, country in enumerate(countries):
    plt.text(gdp_growth[i], unemployment_rate[i], country, ha='center', va='center', fontsize=9)

# Show the plot
plt.tight_layout()
plt.show()