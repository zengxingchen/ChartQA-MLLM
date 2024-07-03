
import matplotlib.pyplot as plt

countries = ['Norway', 'Finland', 'South Korea', 'Japan', 'United States', 'Canada', 'Brazil', 'India', 'China', 'South Africa',
             'Germany', 'France', 'United Kingdom', 'Australia', 'Mexico', 'Russia', 'Nigeria', 'Indonesia', 'Argentina', 'Turkey',
             'Spain', 'Italy', 'Netherlands', 'Sweden']
life_expectancy = [82.9, 81.7, 82.8, 84.6, 78.9, 82.0, 75.9, 69.4, 76.9, 64.1,
                   81.1, 82.4, 81.2, 83.4, 76.1, 72.6, 54.3, 71.5, 76.4, 78.5,
                   83.5, 83.2, 82.1, 82.4]
healthcare_spending = [10.5, 9.1, 8.1, 10.9, 16.9, 10.7, 9.6, 3.5, 5.3, 8.1,
                       11.2, 11.5, 10.0, 9.4, 5.9, 5.1, 3.8, 3.1, 8.2, 6.3,
                       9.2, 8.9, 10.1, 10.9]
gdp = [434.2, 286.8, 1781.9, 4937.5, 21433.2, 1736.4, 1445.2, 2875.1, 14140.2, 351.4,
       3806.1, 2778.7, 2827.1, 1392.7, 1260.6, 1638.8, 432.3, 1051.9, 450.5, 754.0,
       1354.1, 1921.5, 912.9, 541.1]

max_gdp = max(gdp)
bubble_sizes = [(g / max_gdp) * 1000 for g in gdp]

plt.figure(figsize=(20, 12))
plt.scatter(healthcare_spending, life_expectancy, s=bubble_sizes,
            color=['#377eb8', '#ff7f00', '#4daf4a', '#e41a1c', '#984ea3', '#ff33cc', '#a65628', '#f781bf', '#999999', '#66c2a5',
                   '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3', '#1f78b4', '#b15928', '#33a02c',
                   '#6a3d9a', '#b2df8a', '#fb9a99', '#cab2d6'],
            alpha=0.6)

plt.title('Healthcare Spending vs. Life Expectancy by Country', fontsize=18, y=1.05)
plt.xlabel('Healthcare Spending (% of GDP)', fontsize=14)
plt.ylabel('Life Expectancy (years)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)

for i, country in enumerate(countries):
    plt.text(healthcare_spending[i], life_expectancy[i], country, ha='center', va='center', fontsize=10)

plt.tight_layout()
plt.show()