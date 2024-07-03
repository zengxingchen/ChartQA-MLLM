
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'City': ['Beachside', 'Hilltown', 'Desert Oasis', 'Forestville', 'Metrocity',
             'Riverbend', 'Countryside', 'Lakeside', 'Mountain Peak', 'Historical City',
             'Cultural Hub', 'Adventure Park', 'Urban Jungle', 'Seaside Resort', 
             'Eco Village', 'Remote Island', 'Wilderness', 'Coastal City', 'Safari Camp', 'Snowy Town'],
    'Visitors': [1500000, 900000, 700000, 400000, 2300000,
                 800000, 650000, 500000, 300000, 750000,
                 1200000, 450000, 850000, 950000, 
                 600000, 200000, 100000, 700000, 300000, 400000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14,10))

colors = ['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2',
          '#FF7F50', '#6495ED', '#DC143C', '#00FA9A', '#FFDAB9',
          '#7B68EE', '#ADFF2F', '#DA70D6', '#FF69B4', '#1E90FF',
          '#8B4513', '#FF4500', '#2E8B57', '#D2691E', '#5F9EA0']

squarify.plot(sizes=df['Visitors'], label=df['City'], color=colors, alpha=0.7)

plt.title('Visitor Distribution Across Various Travel Destinations', fontsize=18)

plt.axis('off')

plt.show()