import matplotlib.pyplot as plt
import numpy as np

data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'USA': [20, 25, 30, 35, 40],
    'China': [30, 35, 25, 20, 25],
    'India': [25, 20, 20, 25, 15],
    'Germany': [15, 10, 15, 10, 10],
    'France': [10, 10, 10, 10, 10]
}

labels = data['Year']
usa = data['USA']
china = data['China']
india = data['India']
germany = data['Germany']
france = data['France']

width = 0.85
bar_width = 0.4
fig, ax = plt.subplots(figsize=(10, 6))

bar1 = np.add(usa, china).tolist()
bar2 = np.add(bar1, india).tolist()
bar3 = np.add(bar2, germany).tolist()

ax.barh(labels, usa, color='#1f77b4', edgecolor='white', height=bar_width, label='USA')
ax.barh(labels, china, left=usa, color='#ff7f0e', edgecolor='white', height=bar_width, label='China')
ax.barh(labels, india, left=bar1, color='#2ca02c', edgecolor='white', height=bar_width, label='India')
ax.barh(labels, germany, left=bar2, color='#d62728', edgecolor='white', height=bar_width, label='Germany')
ax.barh(labels, france, left=bar3, color='#9467bd', edgecolor='white', height=bar_width, label='France')

ax.set_xlabel('Percentage (%)')
ax.set_title('Renewable Energy Adoption by Country (2018-2022)')
ax.legend(loc='lower right')

plt.show()