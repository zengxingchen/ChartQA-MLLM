
import matplotlib.pyplot as plt

# Data for plotting
countries = ["United States", "China", "Japan", "Germany", "India",
             "United Kingdom", "France", "Brazil", "Italy", "Canada",
             "Russia", "South Korea", "Spain", "Australia", "Mexico",
             "Indonesia", "Netherlands", "Saudi Arabia", "Turkey", "Switzerland"]
gdp = [21433, 14343, 5081, 3861, 2875, 2827, 2715, 1444, 2001, 1736,
       1690, 1650, 1394, 1390, 1217, 1119, 907, 793, 761, 703]  # in billions
population = [331, 1439, 126, 83, 1380, 68, 65, 213, 60, 38, 146, 52, 47, 25, 129, 276, 17, 35, 84, 9]  # in millions
hdi = [0.926, 0.761, 0.919, 0.947, 0.647, 0.932, 0.901, 0.765, 0.892, 0.929,
       0.824, 0.916, 0.904, 0.944, 0.779, 0.718, 0.944, 0.859, 0.820, 0.955]

# Convert HDI to a size for the plot, with an arbitrary scale factor
sizes = [h * 1000 for h in hdi]

# Create the Bubble Chart
plt.figure(figsize=(14, 10))
for i in range(len(countries)):
    plt.scatter(gdp[i], population[i], s=sizes[i], alpha=0.5,
                c=[(hdi[i]-min(hdi))/(max(hdi)-min(hdi)), 
                0.1, (1-(hdi[i]-min(hdi))/(max(hdi)-min(hdi)))])

plt.title('GDP vs Population Size with HDI as Bubble Size')
plt.xlabel('GDP in Billions USD')
plt.ylabel('Population in Millions')
plt.grid(True)

# Add country labels to bubbles
for i, country in enumerate(countries):
    plt.annotate(country, (gdp[i], population[i]), textcoords="offset points", 
                 xytext=(0, 10), ha='center')

plt.show()