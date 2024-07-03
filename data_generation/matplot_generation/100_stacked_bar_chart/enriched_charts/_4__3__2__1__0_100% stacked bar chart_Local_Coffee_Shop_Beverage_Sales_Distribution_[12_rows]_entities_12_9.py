
import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2024)
spring = np.array([15, 18, 20, 22, 25, 30, 28, 25, 30, 35, 32, 30, 33, 35])
rainy_season = np.array([55, 50, 45, 48, 50, 45, 50, 53, 48, 45, 40, 50, 47, 45])
winter = np.array([30, 32, 35, 30, 25, 25, 22, 22, 22, 20, 28, 20, 20, 20])

# Plotting
fig, ax = plt.subplots(figsize=(10, 14))
bar_width = 0.6

# Stacked bar chart
ax.bar(years, spring, color='#FF6347', edgecolor='grey', width=bar_width, label='Spring')
ax.bar(years, rainy_season, bottom=spring, color='#4682B4', edgecolor='grey', width=bar_width, label='Rainy Season')
ax.bar(years, winter, bottom=spring + rainy_season, color='#FFD700', edgecolor='grey', width=bar_width, label='Winter')

# Labels and title
ax.set_ylabel('Percentage')
ax.set_xlabel('Year')
ax.set_title('Annual Rainfall Distribution (2010-2023)', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1), ncol=1)

# Display the chart
plt.tight_layout()
plt.show()