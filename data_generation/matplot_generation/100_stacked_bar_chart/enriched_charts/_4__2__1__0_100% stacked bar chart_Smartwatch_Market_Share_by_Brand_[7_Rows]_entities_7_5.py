
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['2019', '2020', '2021', '2022', '2023', '2024', '2025'],
    'Asia': [20, 25, 30, 25, 20, 35, 25],
    'Europe': [30, 20, 25, 25, 30, 20, 30],
    'North America': [25, 30, 20, 25, 20, 25, 20],
    'South America': [25, 25, 25, 25, 30, 20, 25]
}

categories = data['Category']
asia = np.array(data['Asia'])
europe = np.array(data['Europe'])
north_america = np.array(data['North America'])
south_america = np.array(data['South America'])

bar_width = 0.6

fig, ax = plt.subplots(figsize=(10, 14))

ax.bar(categories, asia, color='#FF6666', edgecolor='white', width=bar_width, label='Asia')
ax.bar(categories, europe, bottom=asia, color='#66B2FF', edgecolor='white', width=bar_width, label='Europe')
ax.bar(categories, north_america, bottom=asia+europe, color='#99FF66', edgecolor='white', width=bar_width, label='North America')
ax.bar(categories, south_america, bottom=asia+europe+north_america, color='#FFD700', edgecolor='white', width=bar_width, label='South America')

ax.set_ylabel('Percentage')
ax.set_title('Annual Distribution of Travel Expenditure by Continent (2019-2025)', pad=20)
ax.legend(loc='upper left')

plt.show()