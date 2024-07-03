
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Primary School', 'Secondary School', 'Higher Education', 'Vocational Training', 'Adult Education']
north_america = [20, 30, 25, 15, 10]
europe = [25, 35, 20, 10, 20]
asia = [30, 25, 30, 20, 15]
africa = [10, 15, 35, 30, 10]
south_america = [15, 20, 25, 25, 25]

# Stack the bars
bar_width = 0.75
indices = np.arange(len(categories))

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(indices, north_america, bar_width, label='North America', color='#4daf4a')
ax.bar(indices, europe, bar_width, bottom=north_america, label='Europe', color='#377eb8')
ax.bar(indices, asia, bar_width, bottom=np.array(north_america) + np.array(europe), label='Asia', color='#ff7f00')
ax.bar(indices, africa, bar_width, bottom=np.array(north_america) + np.array(europe) + np.array(asia), label='Africa', color='#984ea3')
ax.bar(indices, south_america, bar_width, bottom=np.array(north_america) + np.array(europe) + np.array(asia) + np.array(africa), label='South America', color='#e41a1c')

# Add labels
ax.set_ylabel('Percentage')
ax.set_title('Education Participation by Continent', pad=20)
ax.set_xticks(indices)
ax.set_xticklabels(categories)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)

plt.show()