
import matplotlib.pyplot as plt
import pandas as pd
import squarify  # treemap library

# Prepare the data
data = {
    'Region': ['North America', 'North America', 'North America', 'Europe', 'Europe', 
               'Europe', 'Asia', 'Asia', 'Asia', 'South America', 'South America', 'South America',
               'Africa', 'Africa', 'Africa', 'Oceania', 'Oceania', 'Oceania'],
    'Attraction': ['Grand Canyon', 'Niagara Falls', 'Yellowstone', 'Eiffel Tower', 'Colosseum', 
                   'Louvre Museum', 'Great Wall of China', 'Taj Mahal', 'Mount Fuji', 'Christ the Redeemer', 
                   'Machu Picchu', 'Amazon Rainforest', 'Victoria Falls', 'Pyramids of Giza', 
                   'Serengeti National Park', 'Great Barrier Reef', 'Sydney Opera House', 'Fiji Islands'],
    'Visits': [3000, 5000, 2500, 7000, 6500, 6000, 8000, 7500, 4000, 4500, 5000, 3500, 3000, 4000, 3500, 4500, 5000, 3000]
}

df = pd.DataFrame(data)

# Create a color list
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', 
          '#ffd92f', '#e5c494', '#b3b3b3', '#1b9e77', '#d95f02', 
          '#7570b3', '#e7298a', '#66a61e', '#e6ab02', '#a6761d', 
          '#666666', '#1b9e77', '#d95f02']

# Create a figure with a defined size
plt.figure(figsize=(18, 10))

# Plot
squarify.plot(sizes=df['Visits'], label=df['Attraction'], color=colors, alpha=0.8)
plt.title('Number of Tourist Visits to Various Attractions', fontsize=24, y=1.05)

# Remove axes
plt.axis('off')

# Show the plot
plt.show()