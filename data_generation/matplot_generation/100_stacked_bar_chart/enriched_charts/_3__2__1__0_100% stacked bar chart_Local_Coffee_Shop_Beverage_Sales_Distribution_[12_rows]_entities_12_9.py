
import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2024)
renewable = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
non_renewable = np.array([70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5])
other = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.6

# Stacked bar chart
ax.barh(years, renewable, color='#2E8B57', edgecolor='grey', height=bar_width, label='Renewable Energy')
ax.barh(years, non_renewable, left=renewable, color='#4682B4', edgecolor='grey', height=bar_width, label='Non-Renewable Energy')
ax.barh(years, other, left=renewable + non_renewable, color='#FFD700', edgecolor='grey', height=bar_width, label='Other')

# Labels and title
ax.set_xlabel('Percentage')
ax.set_ylabel('Year')
ax.set_title('Energy Consumption Trends (2010-2023)', pad=20)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)

# Display the chart
plt.tight_layout()
plt.show()