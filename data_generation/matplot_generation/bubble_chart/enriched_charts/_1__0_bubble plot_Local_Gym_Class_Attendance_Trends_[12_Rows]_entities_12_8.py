
import matplotlib.pyplot as plt

# Data for plotting
countries = ["Australia", "Brazil", "Canada", "China", "France",
             "Germany", "India", "Indonesia", "Italy", "Japan",
             "Mexico", "Netherlands", "Russia", "Saudi Arabia", "South Korea",
             "Spain", "Switzerland", "Turkey", "United Kingdom", "United States",
             "Nigeria", "Argentina", "Egypt", "Pakistan", "Vietnam"]
population = [25, 213, 38, 1439, 65,
              83, 1380, 276, 60, 126,
              129, 17, 146, 35, 52,
              47, 9, 84, 68, 331,
              206, 45, 102, 220, 97]  # in millions
gdp = [1390, 1444, 1736, 14343, 2715,
       3861, 2875, 1119, 2001, 5081,
       1217, 907, 1690, 793, 1650,
       1394, 703, 761, 2827, 21433,
       450, 486, 365, 314, 340]  # in billions
health_index = [0.944, 0.765, 0.929, 0.761, 0.901,
                0.947, 0.647, 0.718, 0.892, 0.919,
                0.779, 0.944, 0.824, 0.859, 0.916,
                0.904, 0.955, 0.820, 0.932, 0.926,
                0.534, 0.830, 0.707, 0.560, 0.693]

# Convert Health Index to a size for the plot, with an arbitrary scale factor
sizes = [h * 1000 for h in health_index]

# Create the Bubble Chart
plt.figure(figsize=(16, 12))
for i in range(len(countries)):
    plt.scatter(gdp[i], population[i], s=sizes[i], alpha=0.6,
                c=[(health_index[i]-min(health_index))/(max(health_index)-min(health_index)), 
                0.3, (1-(health_index[i]-min(health_index))/(max(health_index)-min(health_index)))],
                edgecolors='w', linewidth=0.5)

plt.title('GDP vs Population Size with Health Index as Bubble Size')
plt.xlabel('GDP in Billions USD')
plt.ylabel('Population in Millions')
plt.grid(True)

# Add country labels to bubbles
for i, country in enumerate(countries):
    plt.annotate(country, (gdp[i], population[i]), textcoords="offset points", 
                 xytext=(0, 10), ha='center', fontsize=8, color='#444444')

plt.show()