
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the treemap
data = {
    'Topic': ['Biology', 'Physics', 'Chemistry', 'Astronomy', 'Geology', 'Meteorology', 'Ecology', 
              'Oceanography', 'Botany', 'Zoology', 'Genetics', 'Evolutionary Biology', 'Marine Biology', 
              'Environmental Science', 'Paleontology', 'Microbiology'],
    'Participants': [500, 400, 350, 300, 250, 200, 150, 120, 100, 80, 60, 50, 40, 30, 20, 10],
    'Percentage': [0.20, 0.16, 0.14, 0.12, 0.10, 0.08, 0.06, 0.048, 0.04, 0.032, 0.024, 0.02, 0.016, 0.012, 0.008, 0.004]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define color list
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#A133FF', '#FF8333', 
          '#33FF83', '#8333FF', '#FF33E0', '#33FFE0', '#E033FF', '#FFEB33', '#FF33EB', 
          '#33EBFF', '#FF3333']

# Plot the Treemap
plt.figure(figsize=(16, 12))
squarify.plot(sizes=df['Percentage'], label=df['Topic'], color=colors, alpha=0.8)
plt.title('Interest in Various Science & Nature Topics among Participants', fontsize=20, pad=20)
plt.axis('off')
plt.show()