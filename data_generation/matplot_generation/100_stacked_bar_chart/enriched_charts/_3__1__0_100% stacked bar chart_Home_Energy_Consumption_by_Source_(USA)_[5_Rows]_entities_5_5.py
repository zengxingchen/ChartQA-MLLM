import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    'Urban': [40, 42, 44, 43, 41, 45, 47, 46, 48, 49, 50, 51, 53, 54],
    'Suburban': [35, 33, 32, 34, 36, 35, 34, 33, 32, 30, 30, 29, 28, 27],
    'Rural': [25, 25, 24, 23, 23, 20, 19, 21, 20, 21, 20, 20, 19, 19]
}

categories = data['Category']
urban = data['Urban']
suburban = data['Suburban']
rural = data['Rural']

barWidth = 0.85
r = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(14, 7))

bars_urban = np.add(suburban, rural).tolist()
bars_suburban = rural

ax.barh(r, rural, color='#d73027', edgecolor='white', height=barWidth)
ax.barh(r, suburban, left=rural, color='#fc8d59', edgecolor='white', height=barWidth)
ax.barh(r, urban, left=bars_urban, color='#91bfdb', edgecolor='white', height=barWidth)

ax.set_yticks(r)
ax.set_yticklabels(categories)
ax.set_xlabel('Percentage')
ax.set_title('Population Distribution Over Time')

plt.legend(['Rural', 'Suburban', 'Urban'], loc='lower right', bbox_to_anchor=(1.15, 0.5))
plt.tight_layout()
plt.show()