
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Japan', 'Germany', 'India',
             'United Kingdom', 'France', 'Italy', 'Brazil', 'Canada',
             'Russia', 'South Korea', 'Spain', 'Australia', 'Mexico']
co2_emissions = [5000, 9000, 1200, 800, 2200,
                 400, 350, 300, 450, 700,
                 1500, 650, 275, 450, 375]

# Create bar chart
plt.figure(figsize=(12, 7))  # Change width and height of the chart
colors = ['#FF5733', '#33FF57', '#3357FF', '#F033FF', '#33FFF0',
          '#FF33A6', '#FFAF33', '#33FFB8', '#B833FF', '#FF8F33',
          '#33D4FF', '#FF3333', '#33FF33', '#FF3380', '#33FF80']

plt.bar(countries, co2_emissions, color=colors, width=0.6)  # Change direction of chart and bar width

# Customizing the plot
plt.ylabel('CO2 Emissions in Million Metric Tons')
plt.title('CO2 Emissions by Country (2020)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Setting y-axis limits to start from a specific value other than zero
plt.ylim(200, 10000)

plt.tight_layout()
plt.show()