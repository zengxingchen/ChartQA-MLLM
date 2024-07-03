
import matplotlib.pyplot as plt

# Table data represented as lists
countries = ['USA', 'China', 'India', 'Germany', 'Brazil', 'UK', 'France', 'Japan', 'Australia', 'Canada', 'South Korea', 'Italy']
years = ['2020', '2021', '2022', '2023']
values = [
    [500, 520, 540, 560],
    [450, 470, 490, 510],
    [300, 320, 340, 360],
    [250, 260, 270, 280],
    [200, 210, 220, 230],
    [180, 190, 200, 210],
    [160, 170, 180, 190],
    [140, 150, 160, 170],
    [120, 130, 140, 150],
    [100, 110, 120, 130],
    [80, 90, 100, 110],
    [60, 70, 80, 90]
]

colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A6', 
          '#33FFF6', '#F633FF', '#F6FF33', '#33A6FF', '#A6FF33',
          '#FF8C33', '#A6FF33']

# Setting the size of the plot
plt.figure(figsize=(14, 8))

# Creating a horizontal bar chart
for i, year in enumerate(years):
    plt.barh(countries, [values[j][i] for j in range(len(countries))], color=colors, edgecolor='grey', height=0.15, left=[sum(values[j][:i]) for j in range(len(countries))], label=year)

# Customizing the plot
plt.xlabel('Values (in thousands)')
plt.title('Annual Value by Country')
plt.xlim(0, max([sum(v) for v in values]) + 100)  # Adjusting x-axis limits for better clarity
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Adding a grid for the x-axis
plt.legend(title='Year')

# Display the plot
plt.show()