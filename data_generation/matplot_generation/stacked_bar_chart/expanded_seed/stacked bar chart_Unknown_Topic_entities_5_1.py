
import matplotlib.pyplot as plt

# Data from the provided table
data = [
    {'Year': 2019, 'Paper': 1400, 'Glass': 1200, 'Metal': 800, 'Plastics': 950},
    {'Year': 2020, 'Paper': 1550, 'Glass': 1300, 'Metal': 870, 'Plastics': 1100},
    {'Year': 2021, 'Paper': 1600, 'Glass': 1350, 'Metal': 900, 'Plastics': 1200},
    {'Year': 2022, 'Paper': 1650, 'Glass': 1400, 'Metal': 950, 'Plastics': 1300},
    {'Year': 2023, 'Paper': 1700, 'Glass': 1450, 'Metal': 1000, 'Plastics': 1350}
]

# Extracting information for each category
years = [item['Year'] for item in data]
papers = [item['Paper'] for item in data]
glasses = [item['Glass'] for item in data]
metals = [item['Metal'] for item in data]
plastics = [item['Plastics'] for item in data]

# Defining the bottom of each stack
bottom_glass = papers
bottom_metal = [p + g for p, g in zip(papers, glasses)]
bottom_plastics = [p + g + m for p, g, m in zip(papers, glasses, metals)]

# Stacked bar chart
plt.bar(years, papers, label='Paper', color='skyblue')
plt.bar(years, glasses, bottom=bottom_glass, label='Glass', color='olivedrab')
plt.bar(years, metals, bottom=bottom_metal, label='Metal', color='lightcoral')
plt.bar(years, plastics, bottom=bottom_plastics, label='Plastics', color='gold')

# Adding lables, title, and custom x-axis ticks
plt.xlabel('Year')
plt.ylabel('Recycling Quantities')
plt.title('Recycling Quantities by Material and Year')
plt.xticks(years, [str(year) for year in years])

# Adding a legend
plt.legend()

# Display the plot
plt.show()