
import matplotlib.pyplot as plt

countries = ['United States', 'Canada', 'Germany', 'United Kingdom', 'France', 'Australia', 'Japan', 'China', 'India', 'Brazil', 'Russia', 'South Africa', 'Nigeria', 'Mexico', 'Indonesia', 'Turkey', 'Argentina', 'South Korea', 'Italy', 'Spain', 'Saudi Arabia', 'Sweden', 'Norway', 'Switzerland', 'Netherlands', 'Belgium', 'Austria', 'Denmark', 'Greece', 'Portugal']
average_life_expectancy = [78.9, 82.3, 81.2, 81.0, 82.4, 82.8, 84.6, 76.4, 69.4, 75.7, 73.1, 63.6, 54.7, 75.0, 71.7, 77.4, 76.5, 83.3, 83.5, 83.4, 75.0, 82.6, 82.5, 83.6, 82.1, 81.4, 81.9, 81.2, 81.0, 81.6]
average_health_expenditure = [10624, 5780, 6665, 4000, 4826, 5274, 4710, 501, 154, 1008, 1460, 525, 78, 1118, 112, 953, 926, 3078, 3624, 3441, 2615, 5831, 7230, 9847, 5154, 5078, 5460, 6187, 2053, 2566]
gdp_per_capita = [63000, 48400, 51600, 43000, 41800, 54900, 42600, 10800, 2200, 8900, 11300, 6000, 2400, 10200, 4100, 10100, 8900, 32500, 34400, 30100, 23400, 54100, 75700, 81700, 52900, 46400, 51500, 60100, 22000, 23900]

bubble_size = [gdp / 1000 for gdp in gdp_per_capita]

plt.figure(figsize=(18, 10))

plt.scatter(average_life_expectancy, average_health_expenditure, s=bubble_size, color=['#FF5733', '#33FF57', '#3357FF', '#FFFF33', '#FF33FF', '#33FFFF', '#5733FF', '#57FF33', '#F3FF33', '#33FFF3', '#FF3357', '#33FF3F', '#FF57F3', '#5733FF', '#FF573F', '#57F3FF', '#33FF57', '#3357F3', '#FFFF33', '#FF33F3', '#33FFFF', '#5733FF', '#57FF33', '#F3FF33', '#33FFF3', '#FF3357', '#33FF3F', '#FF57F3', '#5733FF', '#FF573F'], alpha=0.7, edgecolors='w', linewidth=2)

plt.title('Health Expenditure vs. Life Expectancy in Different Countries', pad=20)
plt.xlabel('Average Life Expectancy (years)')
plt.ylabel('Average Health Expenditure (USD)')

for i, country in enumerate(countries):
    plt.text(average_life_expectancy[i], average_health_expenditure[i], country, ha='center', va='center')

plt.show()