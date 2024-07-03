
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = [
    '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', 
    '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', 
    '2020', '2021', '2022', '2023', '2024'
]
red_planet = [15, 20, 25, 30, 20, 25, 30, 20, 25, 20, 30, 25, 20, 25, 30, 20, 25, 30, 25, 20, 25, 30, 20, 25, 30]
astrobiology = [30, 25, 20, 20, 30, 25, 25, 30, 25, 30, 25, 30, 25, 20, 20, 25, 30, 25, 20, 30, 25, 20, 30, 25, 20]
stellar_obs = [25, 30, 35, 25, 20, 25, 20, 30, 20, 25, 25, 20, 30, 25, 30, 25, 25, 20, 30, 25, 30, 25, 25, 30, 25]
deep_space = [30, 25, 20, 25, 30, 25, 25, 20, 30, 25, 20, 25, 25, 30, 20, 30, 20, 25, 25, 25, 20, 25, 25, 20, 25]

bar_width = 0.8

# Convert data to percentage
total = np.array(red_planet) + np.array(astrobiology) + np.array(stellar_obs) + np.array(deep_space)
red_planet_percent = np.array(red_planet) / total * 100
astrobiology_percent = np.array(astrobiology) / total * 100
stellar_obs_percent = np.array(stellar_obs) / total * 100
deep_space_percent = np.array(deep_space) / total * 100

# Stacked bar chart
fig, ax = plt.subplots(figsize=(14, 8))

ax.bar(categories, red_planet_percent, color='#FF5733', edgecolor='white', width=bar_width, label='Red Planet Exploration')
ax.bar(categories, astrobiology_percent, bottom=red_planet_percent, color='#33FF57', edgecolor='white', width=bar_width, label='Astrobiology Research')
ax.bar(categories, stellar_obs_percent, bottom=red_planet_percent + astrobiology_percent, color='#3357FF', edgecolor='white', width=bar_width, label='Stellar Observations')
ax.bar(categories, deep_space_percent, bottom=red_planet_percent + astrobiology_percent + stellar_obs_percent, color='#FF33A1', edgecolor='white', width=bar_width, label='Deep Space Missions')

# Add title and labels
ax.set_title('NASA Missions Distribution Over Years', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Year')

# Legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()