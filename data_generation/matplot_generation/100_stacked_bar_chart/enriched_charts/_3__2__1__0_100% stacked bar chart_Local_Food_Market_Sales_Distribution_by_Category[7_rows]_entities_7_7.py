
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Classical', 'Jazz', 'Rock', 'Pop', 'Hip Hop', 'Country', 'Electronic']
under_18 = [5, 10, 15, 20, 25, 5, 10]
age_18_24 = [10, 20, 25, 25, 20, 10, 15]
age_25_34 = [20, 25, 20, 15, 10, 15, 20]
age_35_44 = [25, 20, 15, 10, 15, 20, 20]
age_45_54 = [15, 15, 10, 10, 15, 25, 20]
age_55_64 = [15, 5, 10, 10, 10, 15, 10]
age_65_over = [10, 5, 5, 10, 5, 10, 5]

# Bar width
bar_height = 0.8

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(categories, under_18, color='#1f77b4', edgecolor='white', height=bar_height, label='Under 18')
ax.barh(categories, age_18_24, left=np.array(under_18), color='#ff7f0e', edgecolor='white', height=bar_height, label='18-24')
ax.barh(categories, age_25_34, left=np.array(under_18) + np.array(age_18_24), color='#2ca02c', edgecolor='white', height=bar_height, label='25-34')
ax.barh(categories, age_35_44, left=np.array(under_18) + np.array(age_18_24) + np.array(age_25_34), color='#d62728', edgecolor='white', height=bar_height, label='35-44')
ax.barh(categories, age_45_54, left=np.array(under_18) + np.array(age_18_24) + np.array(age_25_34) + np.array(age_35_44), color='#9467bd', edgecolor='white', height=bar_height, label='45-54')
ax.barh(categories, age_55_64, left=np.array(under_18) + np.array(age_18_24) + np.array(age_25_34) + np.array(age_35_44) + np.array(age_45_54), color='#8c564b', edgecolor='white', height=bar_height, label='55-64')
ax.barh(categories, age_65_over, left=np.array(under_18) + np.array(age_18_24) + np.array(age_25_34) + np.array(age_35_44) + np.array(age_45_54) + np.array(age_55_64), color='#e377c2', edgecolor='white', height=bar_height, label='65 and Over')

# Adding labels
ax.set_xlabel('Percentage')
ax.set_title('Music Preferences by Age Group')
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.05))
plt.tight_layout()
plt.show()