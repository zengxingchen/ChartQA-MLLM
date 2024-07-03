
import matplotlib.pyplot as plt

# Data points
years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020
]
population = [
    126926, 129937, 133045, 136256, 139426, 142500,
    145600, 148750, 150000, 151780, 152500, 152900,
    153000, 153100, 153250, 153400, 153500, 153600,
    153700, 153750, 153800
]

# Plot
plt.figure(figsize=(10, 6))  # Change width and height of the chart
plt.plot(years, population, marker='o', color="#FF6347")  # Modify color scheme and add markers

# Annotations
for year, pop in zip(years, population):
    plt.text(year, pop + 300, f'{pop/1000:.1f}K', ha='center', color='#556B2F')  # Assign annotations for each data point

# Change the topic and labels to fit the topic of "Population Growth"
plt.title("Population Growth Over the Years")  # Modify headline
plt.xlabel("Year")                             # Specify the x-axis label
plt.ylabel("Population")                       # Specify the y-axis label

# Show the chart
plt.tight_layout()  # Adjusts plot to ensure everything fits without overlap
plt.show()