
import matplotlib.pyplot as plt

# Data
countries = ['Norway', 'Switzerland', 'Australia', 'Sweden', 'Germany', 'Canada', 'Japan', 'Netherlands', 'United Kingdom', 'France', 
             'Italy', 'Spain', 'South Korea', 'Singapore', 'New Zealand', 'United States', 'China', 'India', 'Russia', 'Brazil']
life_expectancy = [82.5, 83.6, 83.3, 82.6, 81.2, 82.3, 84.6, 82.0, 81.2, 82.4, 
                   83.4, 83.1, 83.0, 83.5, 82.1, 78.9, 76.9, 69.4, 72.6, 75.7]
healthcare_expenditure = [10.5, 12.1, 9.3, 11.0, 11.3, 10.8, 10.9, 10.5, 10.2, 11.2, 
                          9.5, 9.1, 8.1, 5.1, 9.4, 16.8, 5.3, 3.6, 5.3, 9.2]
population = [5421, 8570, 25600, 10300, 83200, 38000, 126500, 17280, 67800, 65200, 
              60400, 47400, 51200, 5800, 5000, 331000, 1395000, 1380000, 144500, 212500]

# Normalize the population data to use as bubble sizes
max_population = max(population)
bubble_sizes = [(p / max_population) * 1000 for p in population]

# Plot
plt.figure(figsize=(18, 10))  # Adjusted width and height of the chart
plt.scatter(life_expectancy, healthcare_expenditure, s=bubble_sizes,
            color=['#3498DB', '#2ECC71', '#E74C3C', '#9B59B6', '#F1C40F', '#1ABC9C', '#34495E', '#F39C12', '#D35400', '#2C3E50', 
                   '#2980B9', '#27AE60', '#C0392B', '#8E44AD', '#F39C12', '#16A085', '#7F8C8D', '#BDC3C7', '#95A5A6', '#D5DBDB'],
            alpha=0.6)

# Additional Customization
plt.title('Life Expectancy vs. Healthcare Expenditure by Country', pad=20)
plt.xlabel('Life Expectancy (Years)')
plt.ylabel('Healthcare Expenditure (% of GDP)')
plt.xticks(rotation=45)
plt.grid(True)

# Annotating the country names
for i, country in enumerate(countries):
    plt.text(life_expectancy[i], healthcare_expenditure[i], country, ha='center', va='center')

# Show the plot
plt.tight_layout()
plt.show()