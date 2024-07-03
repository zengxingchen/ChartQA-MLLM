
import matplotlib.pyplot as plt

# Data
categories = [
    "Beach", "Mountain", "City", "Forest", "Desert", "Island", 
    "Village", "Countryside", "Lake", "River", "Coast", "Valley", 
    "Prairie", "Plateau", "Cave", "Wetland", "Savanna"
]
years = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030]
popularity = [80, 150, 100, 90, 120, 180, 160, 140, 110, 130, 170, 200, 190, 220, 210, 230, 240]

# Scatter plot
fig, ax = plt.subplots(figsize=(14, 8))  # Adjusted width and height of the chart
scatter = ax.scatter(
    years,
    popularity,
    alpha=0.8,
    c=[
        '#e6194B', '#3cb44b', '#ffe119', '#4363d8', '#f58231',
        '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe',
        '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000',
        '#aaffc3', '#808000'
    ],
    edgecolors='w'
)

# Customizing the looks of the plot
ax.set_title('Travel & Adventure: Year Introduced vs Popularity', pad=20)
ax.set_xlabel('Year Introduced')
ax.set_ylabel('Popularity (Index)')

# Adding the category names as labels next to each point
for i, category in enumerate(categories):
    ax.annotate(category, (years[i], popularity[i]), fontsize=8, ha='right')

plt.show()