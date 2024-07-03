
import matplotlib.pyplot as plt

# Data for scientific discoveries and their impact
topics = ['Gravitational Waves', 'CRISPR Gene Editing', 'Higgs Boson Discovery', 'Quantum Computing',
          'Climate Change Effects', 'Dark Matter Research', 'Artificial Intelligence', 'Stem Cell Research',
          'Renewable Energy Tech', 'Nanotechnology', 'Mars Rover Missions', 'Fusion Energy Research',
          'Exoplanet Discoveries', 'Particle Accelerators', 'DNA Sequencing']

impact_factor = [9.5, 9.2, 9.0, 8.8, 8.7, 8.9, 9.1, 8.5, 8.6, 8.4, 8.8, 8.7, 8.9, 8.5, 8.6]
citations = [8500, 7800, 9200, 7000, 6500, 8700, 8300, 7700, 8000, 7400, 8200, 7600, 8500, 6800, 6900]
readership = [22000, 24000, 20000, 18000, 23000, 19000, 21000, 19500, 20500, 18500, 17500, 19000, 22000, 16000, 17000]

# Normalizing the readership size to be suitable for the bubble size
bubble_size = [r / 100 for r in readership]

# Creating the bubble chart
plt.figure(figsize=(16, 12))
for i in range(len(topics)):
    plt.scatter(impact_factor[i],
                citations[i],
                s=bubble_size[i],  # Bubble sizes
                alpha=0.6,
                label=f'{topics[i]}',  # Label for hover
                c=f'#{(255 - i * 12 % 255):02x}{(i * 25 % 255):02x}{(i * 35 % 255):02x}')  # Unique color for each topic

# Chart title and labels
plt.title('Impact and Citations of Key Scientific Discoveries', pad=40)
plt.xlabel('Impact Factor')
plt.ylabel('Number of Citations')

# Adding legend with just the topic names
plt.legend(loc='upper left', title='Scientific Discoveries')

# Show the plot
plt.show()