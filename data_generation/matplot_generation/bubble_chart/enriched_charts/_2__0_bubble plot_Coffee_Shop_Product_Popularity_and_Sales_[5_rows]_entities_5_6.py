
import matplotlib.pyplot as plt

# Data points
countries = ['Japan', 'Switzerland', 'Singapore', 'Australia', 'Spain', 'Italy',
             'Canada', 'South Korea', 'Norway', 'France', 'Sweden', 'New Zealand']
average_life_expectancy = [84.5, 83.7, 83.2, 82.8, 82.3, 82.1, 82.0, 81.9, 81.7, 81.5, 81.3, 81.1]
average_education_expenditure = [4.5, 5.2, 3.5, 5.0, 4.3, 4.1, 5.3, 3.6, 5.5, 5.1, 5.4, 5.0]
population = [126500000, 8600000, 5700000, 25690000, 47350000, 59600000, 38010000, 51780000, 5400000, 65270000, 10300000, 5080000]

# Bubble size is scaled by population (This is a simplification; typically, you would want to scale these values appropriately)
bubble_size = [pop / 1000000 for pop in population]

# Set the figure size
plt.figure(figsize=(16, 9))

# Create the scatter plot
plt.scatter(average_life_expectancy, average_education_expenditure, s=bubble_size,
            color=['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', '#FF5733', '#33FF57', '#3357FF', '#FFFF33', '#FF33FF', '#33FFFF'],
            alpha=0.7, edgecolors='w', linewidth=2)

# Title and labels
plt.title('Life Expectancy vs. Education Expenditure in Various Countries')
plt.xlabel('Average Life Expectancy (years)')
plt.ylabel('Average Education Expenditure (% of GDP)')

# Add country labels to the bubbles
for i, country in enumerate(countries):
    plt.text(average_life_expectancy[i], average_education_expenditure[i], country, ha='center', va='center')

# Show plot
plt.show()