
import matplotlib.pyplot as plt
import squarify

# Dataset
animal_groups = [
    'Insects', 'Arachnids', 'Mollusks', 'Crustaceans', 'Corals', 'Fish', 
    'Amphibians', 'Reptiles', 'Birds', 'Mammals', 'Cnidarians', 'Echinoderms', 
    'Annelids', 'Platyhelminthes', 'Nematodes', 'Poriferans'
]
species_count = [
    1000000, 100000, 85000, 70000, 80000, 33000, 7000, 11000, 10000, 5500, 
    10000, 6000, 17000, 20000, 25000, 10000
]

# Color Scheme
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#5710FF', '#FFD433', '#D4FF33', 
    '#D633FF', '#FF3357', '#33FFD4', '#571033', '#5733FF', '#FF5733', 
    '#33D4FF', '#57FF33', '#FFF333', '#FF33D4'
]

plt.figure(figsize=(14, 10))

# Creating the treemap
squarify.plot(sizes=species_count, label=animal_groups, color=colors, alpha=0.7)

# Adding a title
plt.title('Discovered Species Count in Various Animal Groups', fontsize=16, weight='bold')

# Removing the axes
plt.axis('off')

# Display the plot
plt.show()