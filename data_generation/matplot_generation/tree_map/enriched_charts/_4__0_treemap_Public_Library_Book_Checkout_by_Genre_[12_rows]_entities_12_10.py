
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Prepare the data
data = {
    'Continent': ['Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Africa', 'Africa', 'Africa',
                  'North America', 'North America', 'North America', 'South America', 'South America',
                  'South America', 'Oceania', 'Oceania', 'Oceania', 'Europe', 'Europe', 'Europe', 
                  'Asia', 'Asia', 'Asia', 'Asia', 'Africa', 'Africa', 'Africa', 'North America', 
                  'North America', 'South America', 'Oceania'],
    'Country': ['China', 'India', 'Indonesia', 'Russia', 'Germany', 'United Kingdom', 'Nigeria',
                'Ethiopia', 'Egypt', 'United States', 'Mexico', 'Canada', 'Brazil', 'Colombia',
                'Argentina', 'Australia', 'Papua New Guinea', 'New Zealand', 'France', 'Italy', 'Spain',
                'Japan', 'South Korea', 'Pakistan', 'Bangladesh', 'South Africa', 'Kenya', 'Tanzania',
                'Guatemala', 'Honduras', 'Chile', 'Fiji'],
    'Population': [1444216107, 1393409038, 276361783, 145912025, 83883596, 68207114, 211400708,
                   120812698, 104258327, 334805269, 130262216, 38388465, 214042665, 51516526,
                   45937624, 25925668, 9264775, 5129293, 65273511, 60317116, 46754778, 
                   126050000, 51635256, 225200000, 166303498, 59308690, 53771296, 59734218,
                   17915567, 9904608, 19116201, 896444]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 10))
colors = ['#FF4500', '#32CD32', '#4682B4', '#FFD700', '#00FFFF', '#FF6347', 
          '#EE82EE', '#8A2BE2', '#DC143C', '#00FF00', '#7FFF00', '#D2691E', 
          '#FF00FF', '#8B0000', '#7B68EE', '#ADFF2F', '#DB7093', '#FFA500', 
          '#1E90FF', '#BA55D3', '#FF1493', '#00FA9A', '#D8BFD8', '#FF8C00', 
          '#C71585', '#00CED1', '#9400D3', '#696969', '#FF0000', '#0000FF', 
          '#708090', '#B0E0E6']
squarify.plot(sizes=df['Population'], label=df['Country'], color=colors, alpha=0.7)
plt.title('Population Distribution by Country and Continent', fontsize=18, pad=20)
plt.axis('off')

plt.show()