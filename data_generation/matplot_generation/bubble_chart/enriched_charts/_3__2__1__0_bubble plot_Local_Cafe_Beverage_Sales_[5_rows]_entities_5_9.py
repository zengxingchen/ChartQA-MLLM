
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
vegetarian = [30, 32, 35, 38, 42, 45, 48, 50, 52, 55]
vegan = [25, 28, 30, 32, 35, 38, 40, 42, 45, 48]
paleo = [20, 22, 25, 27, 30, 32, 35, 38, 40, 42]
keto = [10, 12, 15, 18, 20, 22, 25, 28, 30, 32]
mediterranean = [35, 37, 40, 43, 45, 48, 50, 53, 55, 58]
lowcarb = [15, 18, 20, 22, 25, 28, 30, 32, 35, 38]
glutenfree = [12, 15, 18, 20, 22, 25, 28, 30, 32, 35]

# Bubble sizes
bubble_scale = 50
vegetarian_sizes = np.array(vegetarian) * bubble_scale
vegan_sizes = np.array(vegan) * bubble_scale
paleo_sizes = np.array(paleo) * bubble_scale
keto_sizes = np.array(keto) * bubble_scale
mediterranean_sizes = np.array(mediterranean) * bubble_scale
lowcarb_sizes = np.array(lowcarb) * bubble_scale
glutenfree_sizes = np.array(glutenfree) * bubble_scale

fig, ax = plt.subplots(figsize=(16, 9))

# Create scatter points for each category
ax.scatter(years, vegetarian, s=vegetarian_sizes, color='#FF6347', alpha=0.6, label='Vegetarian')
ax.scatter(years, vegan, s=vegan_sizes, color='#3CB371', alpha=0.6, label='Vegan')
ax.scatter(years, paleo, s=paleo_sizes, color='#FFD700', alpha=0.6, label='Paleo')
ax.scatter(years, keto, s=keto_sizes, color='#1E90FF', alpha=0.6, label='Keto')
ax.scatter(years, mediterranean, s=mediterranean_sizes, color='#FF69B4', alpha=0.6, label='Mediterranean')
ax.scatter(years, lowcarb, s=lowcarb_sizes, color='#8A2BE2', alpha=0.6, label='Low-Carb')
ax.scatter(years, glutenfree, s=glutenfree_sizes, color='#32CD32', alpha=0.6, label='Gluten-Free')

# Chart title and labels
ax.set_title('Popularity of Different Diets Over the Years', fontsize=20, pad=20)
ax.set_xlabel('Year', fontsize=16)
ax.set_ylabel('Number of Followers (in millions)', fontsize=16)

# Legend
ax.legend(loc='upper right', title='Diet Type')

plt.tight_layout()
plt.show()