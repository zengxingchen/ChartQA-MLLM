
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2019', '2020', '2021', '2022']
android = np.array([74.45, 71.93, 70.97, 68.74])
ios = np.array([22.85, 26.99, 27.84, 30.28])
others = np.array([2.70, 1.08, 1.19, 0.98])

# Normalize data
totals = android + ios + others
android_percentage = android / totals * 100
ios_percentage = ios / totals * 100
others_percentage = others / totals * 100

# Colors
colors_android = '#ff9999'
colors_ios = '#66b3ff'
colors_others = '#99ff99'

# Bar width
bar_width = 0.65

# Create bars
bar1 = plt.bar(years, android_percentage, color=colors_android, edgecolor='white', width=bar_width)
bar2 = plt.bar(years, ios_percentage, bottom=android_percentage, color=colors_ios, edgecolor='white', width=bar_width)
bar3 = plt.bar(years, others_percentage, bottom=android_percentage+ios_percentage, color=colors_others, edgecolor='white', width=bar_width)

# Create names on the x-axis
plt.xticks(years)
plt.xlabel('Year')

# Set the title
plt.title('Market Share of Smartphone Operating Systems')

# Custom y-axis to show percentages
plt.yticks(np.arange(0, 101, 10))
plt.ylabel('Percentage (%)')

# Set chart size
plt.gcf().set_size_inches(12, 8)
plt.gca().set_aspect(0.1)

# Add a legend
plt.legend((bar1[0], bar2[0], bar3[0]), ('Android', 'iOS', 'Others'), loc='upper left', bbox_to_anchor=(1,1))

# Show graphic
plt.show()