
import matplotlib.pyplot as plt

# Data
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
          "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", 
          "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte", 
          "Seattle", "Denver", "El Paso", "Detroit", "Boston", 
          "San Francisco", "Miami", "Orlando", "Atlanta"]
population_density = [28317, 8484, 11883, 3796, 3120, 11680, 3303, 4382, 3863, 5757, 
                      3082, 1201, 2872, 3916, 2873, 3425, 4863, 2460, 4903, 13989, 
                      18723, 12011, 2349, 3472]
quality_of_life = [162, 136, 154, 131, 134, 145, 139, 147, 140, 168, 
                   160, 129, 135, 142, 138, 164, 159, 132, 125, 163, 
                   170, 148, 137, 143]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(14, 10))

# Scatter plot
ax.scatter(population_density, quality_of_life, color=["#FF5733", "#33FF57", "#3357FF", "#FF33A8", "#A833FF", 
                                                       "#33FFF5", "#FF8C33", "#57FF33", "#FF3333", "#33FFA8", 
                                                       "#FF5733", "#33FF57", "#3357FF", "#FF33A8", "#A833FF", 
                                                       "#33FFF5", "#FF8C33", "#57FF33", "#FF3333", "#33FFA8",
                                                       "#33FFBD", "#FF5733", "#3357FF", "#FF8C33"])

# Title and labels
plt.title('Quality of Life vs. Population Density in Different Cities', pad=20)
plt.xlabel('Population Density (per sq mile)')
plt.ylabel('Quality of Life Index')

# Show plot
plt.show()