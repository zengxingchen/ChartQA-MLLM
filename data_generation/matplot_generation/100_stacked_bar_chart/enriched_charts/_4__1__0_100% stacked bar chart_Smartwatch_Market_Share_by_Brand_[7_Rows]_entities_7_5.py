
import matplotlib.pyplot as plt
import numpy as np

# Data
ecosystems = ['Forest', 'Desert', 'Ocean', 'Wetland', 'Grassland']
species_a = [25, 10, 30, 20, 15]
species_b = [35, 20, 25, 30, 25]
species_c = [20, 40, 15, 25, 30]
species_d = [15, 20, 20, 15, 20]
species_e = [5, 10, 10, 10, 10]

# Convert to percentage
total = np.array(species_a) + np.array(species_b) + np.array(species_c) + np.array(species_d) + np.array(species_e)
species_a = np.array(species_a) / total * 100
species_b = np.array(species_b) / total * 100
species_c = np.array(species_c) / total * 100
species_d = np.array(species_d) / total * 100
species_e = np.array(species_e) / total * 100

# Plot
fig, ax = plt.subplots(figsize=(10, 8))

bar_width = 0.7

bar1 = ax.bar(ecosystems, species_a, bar_width, color='#FF5733', label='Species A')
bar2 = ax.bar(ecosystems, species_b, bar_width, bottom=species_a, color='#33FF57', label='Species B')
bar3 = ax.bar(ecosystems, species_c, bar_width, bottom=species_a+species_b, color='#3357FF', label='Species C')
bar4 = ax.bar(ecosystems, species_d, bar_width, bottom=species_a+species_b+species_c, color='#FF33A8', label='Species D')
bar5 = ax.bar(ecosystems, species_e, bar_width, bottom=species_a+species_b+species_c+species_d, color='#FFC133', label='Species E')

# Add title and labels
ax.set_title('Distribution of Species in Different Ecosystems', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Ecosystems')

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.show()