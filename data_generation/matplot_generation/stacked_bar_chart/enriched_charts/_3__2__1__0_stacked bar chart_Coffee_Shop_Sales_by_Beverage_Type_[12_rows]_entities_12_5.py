
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
physical = [8000, 8500, 9000, 9500, 10000, 10500, 11000]
emotional = [10000, 10500, 11000, 11500, 12000, 12500, 13000]
mental = [12000, 12500, 13000, 13500, 14000, 14500, 15000]
spiritual = [6000, 6500, 7000, 7500, 8000, 8500, 9000]

# Plot
fig, ax = plt.subplots(figsize=(10, 12))  # Change width and height of the chart

# Vertical bar chart
bar_width = 0.6
ax.bar(years, physical, color='#ff4500', edgecolor='white', width=bar_width)
ax.bar(years, emotional, bottom=physical, color='#1e90ff', edgecolor='white', width=bar_width)
ax.bar(years, mental, bottom=[i+j for i,j in zip(physical, emotional)], color='#32cd32', edgecolor='white', width=bar_width)
ax.bar(years, spiritual, bottom=[i+j+k for i,j,k in zip(physical, emotional, mental)], color='#ff69b4', edgecolor='white', width=bar_width)

# Adding numerical labels
for i in range(len(years)):
    ax.text(i, physical[i]/2, str(physical[i]), va='center', ha='center', color='white', fontweight='bold')
    ax.text(i, physical[i] + emotional[i]/2, str(emotional[i]), va='center', ha='center', color='white', fontweight='bold')
    ax.text(i, physical[i] + emotional[i] + mental[i]/2, str(mental[i]), va='center', ha='center', color='white', fontweight='bold')
    ax.text(i, physical[i] + emotional[i] + mental[i] + spiritual[i]/2, str(spiritual[i]), va='center', ha='center', color='white', fontweight='bold')

ax.set_ylabel('Number of Individuals')
ax.set_title('Well-being Categories from 2015 to 2021')
ax.set_xticks(years)
ax.set_ylim(0, 60000)  # Adjust to accommodate the sum of the data points

plt.show()