
import matplotlib.pyplot as plt

data = {
    'Location': ['Amazon Rainforest', 'Sahara Desert', 'Great Barrier Reef', 'Arctic Tundra', 
                 'Himalayan Mountains', 'Andes Mountains', 'Siberian Taiga', 'Serengeti Plains',
                 'Yellowstone Park', 'Galapagos Islands', 'Australian Outback', 'Amazon Basin',
                 'Patagonian Steppe', 'Congo Rainforest', 'Rocky Mountains'],
    'Climate Score (1-10)': [9.5, 3.1, 8.9, 4.7, 6.8, 7.2, 5.6, 8.4, 7.9, 9.1, 4.3, 8.7, 5.4, 8.6, 6.5],
    'Average Temperature (°C)': [27, 35, 25, -15, -5, 10, -10, 22, 8, 24, 32, 26, 12, 28, 5],
    'Biodiversity Score (1-100)': [95, 20, 85, 70, 50, 65, 45, 80, 75, 90, 30, 88, 40, 89, 60]
}

fig, ax = plt.subplots(figsize=(14, 10))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5']

for i in range(len(data['Location'])):
    ax.scatter(data['Climate Score (1-10)'][i], data['Average Temperature (°C)'][i], 
               s=(data['Biodiversity Score (1-100)'][i] ** 2) / 10,  
               alpha=0.6,
               color=colors[i])  

ax.set_title('Climate Zones: Temperature vs Climate Score with Biodiversity as Bubble Size', fontsize=16)
ax.set_xlabel('Climate Score (1-10)', fontsize=14)
ax.set_ylabel('Average Temperature (°C)', fontsize=14)
ax.grid(True)

plt.show()