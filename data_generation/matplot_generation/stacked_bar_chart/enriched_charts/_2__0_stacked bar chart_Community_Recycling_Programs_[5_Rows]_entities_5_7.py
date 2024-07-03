
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
classical = [10000, 11000, 11500, 12000, 12500, 13000, 13500]
rock = [15000, 16000, 17000, 18000, 19000, 20000, 21000]
pop = [20000, 21000, 22000, 23000, 24000, 25000, 26000]
jazz = [12000, 13000, 14000, 14500, 15000, 15500, 16000]

# Bottom data for stacking
rock_bottom = [i + j for i, j in zip(classical, rock)]
pop_bottom = [i + j for i, j in zip(rock_bottom, pop)]

# Figure and Axes
fig, ax = plt.subplots(figsize=(12, 8))  # Change width and height of the chart

# Stacked Vertical Bars
ax.bar(years, classical, color='#FF6347', edgecolor='white', width=0.4)  # Classical with tomato color
ax.bar(years, rock, bottom=classical, color='#4682B4', edgecolor='white', width=0.4)  # Rock with steel blue color
ax.bar(years, pop, bottom=rock_bottom, color='#32CD32', edgecolor='white', width=0.4)  # Pop with lime green color
ax.bar(years, jazz, bottom=pop_bottom, color='#FFD700', edgecolor='white', width=0.4)  # Jazz with gold color

# Labels and Title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Albums Sold')
ax.set_title('Album Sales by Genre from 2015 to 2021')
for i, val in enumerate(classical):
    ax.text(years[i], val / 2, str(val), ha='center', va='center', color='black')
for i, val in enumerate(rock):
    ax.text(years[i], classical[i] + val / 2, str(val), ha='center', va='center', color='black')
for i, val in enumerate(pop):
    ax.text(years[i], rock_bottom[i] + val / 2, str(val), ha='center', va='center', color='black')
for i, val in enumerate(jazz):
    ax.text(years[i], pop_bottom[i] + val / 2, str(val), ha='center', va='center', color='black')

# Display the plot
plt.show()