
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Attraction': ['Grand Canyon', 'Niagara Falls', 'Eiffel Tower', 'Great Wall of China',
                   'Machu Picchu', 'Pyramids of Giza', 'Christ the Redeemer', 'Colosseum',
                   'Statue of Liberty', 'Sydney Opera House', 'Taj Mahal', 'Disneyland',
                   'Louvre Museum', 'Mount Everest', 'Yellowstone National Park', 'Mount Fuji',
                   'Banff National Park', 'Santorini', 'Venice Canals', 'Galapagos Islands',
                   'Great Barrier Reef', 'Swiss Alps', 'Amazon Rainforest', 'Serengeti National Park'],
    'Visitors': [4500, 6200, 8000, 7500, 5200, 5800, 3000, 7000, 6700, 4900, 8200, 15000, 
                 9200, 2500, 3500, 4000, 3100, 6000, 4300, 3600, 2900, 2700, 2200, 3700]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 10))
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6", "#c4e17f", "#76d7c4", "#f7a35c", "#f45b5b", "#91e8e1", "#2b908f", "#f7a35c", "#7cb5ec", "#434348", "#f15c80", "#e4d354", "#8d4653", "#91e8e1", "#2b908f", "#f7a35c", "#7cb5ec", "#434348", "#f15c80"]
squarify.plot(sizes=df['Visitors'], label=df['Attraction'], alpha=0.8, color=colors)
plt.title('Number of Visitors to Various Natural and Cultural Attractions', fontsize=18)
plt.axis('off')
plt.show()