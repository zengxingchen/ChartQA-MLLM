
import matplotlib.pyplot as plt

# Data
countries = ['China', 'United States', 'India', 'Russia', 'Japan', 'Germany', 'Canada', 'Brazil', 'South Korea', 'Australia', 
             'Mexico', 'Indonesia', 'Nigeria', 'United Kingdom', 'France', 'Italy', 'Spain', 'South Africa', 'Argentina', 'Turkey']
average_temperature = [15.3, 12.6, 24.5, -5.5, 16.2, 10.3, -5.6, 25.0, 11.8, 21.5, 
                       23.2, 26.0, 27.0, 9.7, 11.3, 13.9, 15.5, 17.3, 14.8, 12.5]
annual_rainfall = [600, 715, 1080, 460, 1700, 700, 530, 1750, 1300, 350, 
                   850, 2300, 1200, 1150, 850, 750, 640, 600, 850, 570]
population = [1395000, 331000, 1380000, 144500, 126500, 83200, 38000, 212500, 51200, 25600, 
              127600, 273500, 206000, 67800, 65200, 60400, 47400, 59300, 45100, 84200]

# Normalize the population data to use as bubble sizes
max_population = max(population)
bubble_sizes = [(p / max_population) * 1000 for p in population]

# Plot
plt.figure(figsize=(16, 9))  # Adjusted width and height of the chart
plt.scatter(average_temperature, annual_rainfall, s=bubble_sizes,
            color=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#A133FF', '#FFA133', '#33A1FF', '#FF3333', '#33FF33', 
                   '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#A133FF', '#FFA133', '#33A1FF', '#FF3333', '#33FF33'],
            alpha=0.6)

# Additional Customization
plt.title('Average Temperature vs. Annual Rainfall by Country')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Annual Rainfall (mm)')
plt.xticks(rotation=45)
plt.grid(True)

# Annotating the country names
for i, country in enumerate(countries):
    plt.text(average_temperature[i], annual_rainfall[i], country, ha='center', va='center')

# Show the plot
plt.tight_layout()
plt.show()