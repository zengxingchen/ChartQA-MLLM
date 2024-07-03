
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    'Europe': [35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25],
    'Asia': [40, 41, 43, 42, 44, 45, 46, 47, 48, 49, 50],
    'North America': [15, 16, 15, 16, 15, 14, 15, 15, 14, 14, 15],
    'South America': [5, 4, 5, 6, 6, 7, 6, 6, 7, 7, 6],
    'Africa': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    'Oceania': [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

years = data['Year']
europe = data['Europe']
asia = data['Asia']
north_america = data['North America']
south_america = data['South America']
africa = data['Africa']
oceania = data['Oceania']

barWidth = 0.85

r = np.arange(len(years))

plt.figure(figsize=(14, 8))

plt.barh(r, europe, color='#FF9999', edgecolor='white', height=barWidth, label='Europe')
plt.barh(r, asia, left=europe, color='#66B2FF', edgecolor='white', height=barWidth, label='Asia')
plt.barh(r, north_america, left=np.array(europe)+np.array(asia), color='#99FF99', edgecolor='white', height=barWidth, label='North America')
plt.barh(r, south_america, left=np.array(europe)+np.array(asia)+np.array(north_america), color='#FFCC99', edgecolor='white', height=barWidth, label='South America')
plt.barh(r, africa, left=np.array(europe)+np.array(asia)+np.array(north_america)+np.array(south_america), color='#FFB266', edgecolor='white', height=barWidth, label='Africa')
plt.barh(r, oceania, left=np.array(europe)+np.array(asia)+np.array(north_america)+np.array(south_america)+np.array(africa), color='#B3B3CC', edgecolor='white', height=barWidth, label='Oceania')

plt.xlabel('Percentage')
plt.ylabel('Year')
plt.title('Internet Usage by Continent (2010-2020)', pad=20)
plt.yticks(r, years)
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
plt.tight_layout()
plt.show()