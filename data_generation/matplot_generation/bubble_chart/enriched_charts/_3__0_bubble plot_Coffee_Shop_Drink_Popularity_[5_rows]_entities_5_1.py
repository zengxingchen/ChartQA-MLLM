
import matplotlib.pyplot as plt

data = {
    'City': ['New York', 'Tokyo', 'Paris', 'London', 'Dubai', 'Sydney', 'Rome', 'Barcelona', 'Bangkok', 
             'Los Angeles', 'Beijing', 'Mumbai', 'Toronto', 'Singapore', 'Hong Kong', 'Istanbul', 
             'Cape Town', 'Buenos Aires', 'Moscow', 'Berlin'],
    'Average Temperature (°C)': [13.0, 16.0, 12.0, 11.5, 28.0, 18.0, 15.0, 16.5, 28.5, 18.5, 12.0, 27.0, 9.0, 
                                 27.5, 24.0, 14.0, 17.0, 18.0, 5.8, 9.9],
    'Annual Rainfall (mm)': [1200, 1500, 650, 750, 100, 1200, 800, 600, 1500, 400, 570, 2200, 850, 2300, 2400, 
                             800, 600, 1200, 700, 580],
    'Tourist Visits (millions)': [63, 60, 38, 30, 16, 12, 10, 9, 22, 50, 29, 8, 27, 19, 26, 14, 6, 7, 21, 13]
}

fig, ax = plt.subplots(figsize=(16, 9))

for i in range(len(data['City'])):
    ax.scatter(data['Average Temperature (°C)'][i], data['Annual Rainfall (mm)'][i], 
               s=data['Tourist Visits (millions)'][i] * 5,  
               label='{}'.format(data['City'][i]),
               alpha=0.6, edgecolors='w', linewidth=2)

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF4500', 
          '#8A2BE2', '#00CED1', '#FF69B4', '#BA55D3', '#D2691E', 
          '#1E90FF', '#ADFF2F', '#FF1493', '#8B0000', '#00FF7F', 
          '#B8860B', '#6A5ACD', '#20B2AA', '#FFDAB9', '#8FBC8F']

for i, dot in enumerate(ax.collections):
    dot.set_facecolor(colors[i % len(colors)])

ax.set_title('Bubble Chart: City Average Temperature, Annual Rainfall, and Tourist Visits', pad=20)
ax.set_xlabel('Average Temperature (°C)')
ax.set_ylabel('Annual Rainfall (mm)')

ax.grid(True)
ax.legend(title='Cities', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()