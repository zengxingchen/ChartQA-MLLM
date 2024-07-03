import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['2020', '2021', '2022', '2023'],
    'Health': [25, 30, 20, 25],
    'Education': [30, 25, 25, 20],
    'Entertainment': [20, 25, 30, 25],
    'Technology': [25, 20, 25, 30]
}

categories = data['Category']
health = np.array(data['Health'])
education = np.array(data['Education'])
entertainment = np.array(data['Entertainment'])
technology = np.array(data['Technology'])

bar_width = 0.5

fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(categories, health, color='#FF9999', edgecolor='white', height=bar_width, label='Health')
ax.barh(categories, education, left=health, color='#66B3FF', edgecolor='white', height=bar_width, label='Education')
ax.barh(categories, entertainment, left=health+education, color='#99FF99', edgecolor='white', height=bar_width, label='Entertainment')
ax.barh(categories, technology, left=health+education+entertainment, color='#FFD700', edgecolor='white', height=bar_width, label='Technology')

ax.set_xlabel('Percentage')
ax.set_title('Annual Distribution of Expenditure by Category (2020-2023)', pad=20)
ax.legend(loc='lower right')

plt.show()