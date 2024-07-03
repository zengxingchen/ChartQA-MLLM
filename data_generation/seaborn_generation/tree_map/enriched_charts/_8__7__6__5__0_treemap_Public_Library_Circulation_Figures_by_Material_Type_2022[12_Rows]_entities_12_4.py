
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the treemap
data = {
    'Category': ['Physics', 'Chemistry', 'Biology', 'Astronomy', 'Geology', 'Meteorology',
                 'Ecology', 'Botany', 'Zoology', 'Marine Biology', 'Paleontology', 'Genetics',
                 'Microbiology', 'Entomology', 'Astrophysics', 'Environmental Science',
                 'Anthropology', 'Evolutionary Biology', 'Biochemistry', 'Molecular Biology'],
    'Interest': [1200, 1100, 1050, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150],
    'Percentage': [0.20, 0.1833, 0.175, 0.1583, 0.15, 0.1417, 0.1333, 0.125, 0.1167, 0.1083, 0.10, 0.0917, 0.0833, 0.075, 0.0667, 0.0583, 0.05, 0.0417, 0.0333, 0.025]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define color list
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A1FF33', '#FF5733',
          '#33FFA1', '#A133FF', '#FF3333', '#33FF33', '#5733FF', '#33A1FF',
          '#A1FF57', '#FF5733', '#33FF57', '#5733FF', '#A1FF33', '#33FFA1', 
          '#FF33A1', '#A133FF']

# Plot the Treemap
plt.figure(figsize=(16, 12))
squarify.plot(sizes=df['Percentage'], label=df['Category'], color=colors, alpha=0.8)
plt.title('Interest in Various Science & Nature Categories among Enthusiasts', fontsize=20, pad=20)
plt.axis('off')
plt.show()