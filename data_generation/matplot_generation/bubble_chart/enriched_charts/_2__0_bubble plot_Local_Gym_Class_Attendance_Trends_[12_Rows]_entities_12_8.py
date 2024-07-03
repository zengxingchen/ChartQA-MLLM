import matplotlib.pyplot as plt

# Data for plotting
countries = ["Finland", "Denmark", "Switzerland", "Iceland", "Norway", 
             "Netherlands", "Sweden", "New Zealand", "Austria", "Luxembourg", 
             "Canada", "Australia", "United Kingdom", "Israel", "Germany", 
             "Ireland", "United States", "Czech Republic", "Belgium", "France"]
happiness_scores = [7.8, 7.6, 7.5, 7.5, 7.4, 
                    7.4, 7.3, 7.3, 7.2, 7.2, 
                    7.2, 7.2, 7.1, 7.1, 7.0, 
                    7.0, 6.9, 6.9, 6.8, 6.7]
life_expectancy = [81.8, 80.9, 83.6, 82.4, 82.8, 
                   82.1, 82.6, 82.3, 82.1, 82.3, 
                   82.2, 82.9, 81.4, 82.7, 81.0, 
                   82.3, 78.9, 79.3, 81.6, 82.5]
population = [5.5, 5.8, 8.7, 0.3, 5.4, 
              17.5, 10.4, 4.9, 9.0, 0.6, 
              38.0, 25.7, 67.2, 9.3, 83.0, 
              5.0, 331.0, 10.7, 11.5, 65.3]

# Convert life expectancy to a size for the plot, with an arbitrary scale factor
sizes = [le * 10 for le in life_expectancy]

# Create the Bubble Chart
plt.figure(figsize=(16, 12))
for i in range(len(countries)):
    plt.scatter(happiness_scores[i], population[i], s=sizes[i], alpha=0.5,
                c=[(life_expectancy[i]-min(life_expectancy))/(max(life_expectancy)-min(life_expectancy)), 
                0.1, (1-(life_expectancy[i]-min(life_expectancy))/(max(life_expectancy)-min(life_expectancy)))])

plt.title('Happiness Score vs Population with Life Expectancy as Bubble Size')
plt.xlabel('Happiness Score')
plt.ylabel('Population in Millions')
plt.grid(True)

# Add country labels to bubbles
for i, country in enumerate(countries):
    plt.annotate(country, (happiness_scores[i], population[i]), textcoords="offset points", 
                 xytext=(0, 10), ha='center')

plt.show()