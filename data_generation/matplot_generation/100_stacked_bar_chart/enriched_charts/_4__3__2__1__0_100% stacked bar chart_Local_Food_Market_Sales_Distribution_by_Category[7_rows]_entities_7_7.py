
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Biography', 'Mystery', 'Historical', 'Poetry', 'Classics']
under_18 = [5, 10, 15, 20, 10, 15, 25, 10, 15]
age_18_24 = [15, 20, 25, 25, 15, 10, 10, 10, 15]
age_25_34 = [20, 25, 20, 15, 15, 15, 10, 15, 20]
age_35_44 = [25, 20, 15, 10, 15, 10, 10, 10, 25]
age_45_54 = [20, 15, 10, 10, 20, 15, 10, 5, 10]
age_55_64 = [10, 5, 10, 10, 15, 25, 20, 10, 5]
age_65_over = [5, 5, 5, 10, 10, 10, 15, 5, 5]

# Bar width
bar_width = 0.8

# Plotting
fig, ax = plt.subplots(figsize=(14, 10))
ax.bar(categories, under_18, color='#FF5733', edgecolor='white', width=bar_width, label='Under 18')
ax.bar(categories, age_18_24, bottom=np.array(under_18), color='#33FF57', edgecolor='white', width=bar_width, label='18-24')
ax.bar(categories, age_25_34, bottom=np.array(under_18) + np.array(age_18_24), color='#3357FF', edgecolor='white', width=bar_width, label='25-34')
ax.bar(categories, age_35_44, bottom=np.array(under_18) + np.array(age_18_24) + np.array(age_25_34), color='#FF33A1', edgecolor='white', width=bar_width, label='35-44')
ax.bar(categories, age_45_54, bottom=np.array(under_18) + np.array(age_18_24) + np.array(age_25_34) + np.array(age_35_44), color='#FFC300', edgecolor='white', width=bar_width, label='45-54')
ax.bar(categories, age_55_64, bottom=np.array(under_18) + np.array(age_18_24) + np.array(age_25_34) + np.array(age_35_44) + np.array(age_45_54), color='#DAF7A6', edgecolor='white', width=bar_width, label='55-64')
ax.bar(categories, age_65_over, bottom=np.array(under_18) + np.array(age_18_24) + np.array(age_25_34) + np.array(age_35_44) + np.array(age_45_54) + np.array(age_55_64), color='#900C3F', edgecolor='white', width=bar_width, label='65 and Over')

# Adding labels
ax.set_ylabel('Percentage')
ax.set_title('Literature Preferences by Age Group')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()