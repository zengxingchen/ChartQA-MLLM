
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Location': ['Beachside', 'Hilltown', 'Desert Oasis', 'Forestville', 'Metrocity',
                 'Riverbend', 'Countryside', 'Lakeside', 'Mountain Peak', 'Historical City',
                 'Cultural Hub', 'Adventure Park', 'Urban Jungle', 'Seaside Resort', 
                 'Eco Village', 'Remote Island', 'Wilderness', 'Coastal City', 'Safari Camp', 'Snowy Town',
                 'Solar City', 'Astro Town', 'Galaxy Base', 'Orbital Station', 'Space Colony',
                 'Nebula Village', 'Lunar Outpost', 'Martian City', 'Stellar Port', 'Cosmic Hub'],
    'Value': [1500000, 900000, 700000, 400000, 2300000,
              800000, 650000, 500000, 300000, 750000,
              1200000, 450000, 850000, 950000, 
              600000, 200000, 100000, 700000, 300000, 400000,
              1100000, 950000, 1250000, 850000, 450000,
              2000000, 900000, 3000000, 1700000, 1400000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16,12))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#57FF33',
          '#5733FF', '#FF5733', '#33FF57', '#3357FF', '#FF33A1',
          '#57FF33', '#5733FF', '#FF5733', '#33FF57', '#3357FF',
          '#FF33A1', '#57FF33', '#5733FF', '#FF5733', '#33FF57',
          '#3357FF', '#FF33A1', '#57FF33', '#5733FF', '#FF5733',
          '#33FF57', '#3357FF', '#FF33A1', '#57FF33', '#5733FF']

squarify.plot(sizes=df['Value'], label=df['Location'], color=colors, alpha=0.7)

plt.title('Population Distribution in Future Space Colonies', fontsize=20)

plt.axis('off')

plt.show()