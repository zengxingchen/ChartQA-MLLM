
import matplotlib.pyplot as plt

# Data
species = ['Elephant', 'Tiger', 'Panda', 'Kangaroo', 'Giraffe', 
           'Rhinoceros', 'Lion', 'Hippopotamus', 'Gorilla', 'Orangutan', 
           'Zebra', 'Polar Bear', 'Leopard', 'Cheetah', 'Chimpanzee', 
           'Koala', 'Sloth', 'Otter', 'Meerkat']
population = [415000, 3900, 1864, 50000, 68000, 
              27500, 20000, 130000, 1000, 104700, 
              750000, 26000, 70000, 7100, 172700, 
              80000, 150000, 106000, 1000000]  # in numbers
height = [3.3, 0.9, 0.75, 1.5, 5.5, 
          1.8, 1.2, 1.5, 1.75, 1.4, 
          1.3, 1.6, 0.7, 0.8, 1.3, 
          0.85, 0.6, 0.3, 0.25]  # in meters
weight = [6000, 300, 100, 85, 800, 
          2300, 190, 1500, 160, 90, 
          450, 450, 90, 72, 60, 
          15, 8, 12, 1]  # in kg

# Color for each species
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
          '#1f78b4', '#ff7790', '#2c7a2c', '#d68228', '#9462bd', 
          '#8c567b', '#e377c3', '#7f8f7f', '#bc1d22']

# Using weight as the size of the bubble
sizes = [w / max(weight) * 2000 for w in weight]

# Set up the figure size
plt.figure(figsize=(18, 14))

# Scatter plot
plt.scatter(population, height, s=sizes, c=colors, alpha=0.6)

# Labels and Title
plt.title('Bubble Chart of Animal Populations, Heights, and Weights', fontsize=20)
plt.xlabel('Population (number of individuals)', fontsize=16)
plt.ylabel('Height (meters)', fontsize=16)

# Add species names to the bubbles
for i, specie in enumerate(species):
    plt.annotate(specie, (population[i], height[i]), fontsize=12)

# Show grid
plt.grid(True)

# Show the plot
plt.show()