
import matplotlib.pyplot as plt
import numpy as np

# Given data points
years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
adventure_travel = [10, 15, 20, 25, 30, 35, 20, 25]
cultural_travel = [25, 30, 20, 25, 15, 20, 25, 30]
nature_travel = [30, 25, 25, 20, 15, 10, 25, 20]
recreational_travel = [35, 30, 35, 30, 40, 35, 30, 25]

# Convert the data to percentage
total = [sum(x) for x in zip(adventure_travel, cultural_travel, nature_travel, recreational_travel)]
adventure_travel_percentage = [i / j * 100 for i, j in zip(adventure_travel, total)]
cultural_travel_percentage = [i / j * 100 for i, j in zip(cultural_travel, total)]
nature_travel_percentage = [i / j * 100 for i, j in zip(nature_travel, total)]
recreational_travel_percentage = [i / j * 100 for i, j in zip(recreational_travel, total)]

# Set the figure size
plt.figure(figsize=(12, 10))

# Plot vertical bar chart
barWidth = 0.65
plt.bar(years, adventure_travel_percentage, color='#4daf4a', edgecolor='white', width=barWidth, label='Adventure Travel')
plt.bar(years, cultural_travel_percentage, bottom=adventure_travel_percentage, color='#377eb8', edgecolor='white', width=barWidth, label='Cultural Travel')
plt.bar(years, nature_travel_percentage, bottom=[i+j for i,j in zip(adventure_travel_percentage, cultural_travel_percentage)], color='#ff7f00', edgecolor='white', width=barWidth, label='Nature Travel')
plt.bar(years, recreational_travel_percentage, bottom=[i+j+k for i,j,k in zip(adventure_travel_percentage, cultural_travel_percentage, nature_travel_percentage)], color='#e41a1c', edgecolor='white', width=barWidth, label='Recreational Travel')

# Add a legend
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Travel Categories')

# Add labels and title
plt.ylabel('Percentage')
plt.title('Travel Preferences Over the Years', pad=20)

# Change ylim for better spacing
plt.ylim(0, 100)

# Display the plot
plt.show()