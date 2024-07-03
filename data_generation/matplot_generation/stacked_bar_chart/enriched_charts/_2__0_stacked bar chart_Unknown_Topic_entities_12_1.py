
import matplotlib.pyplot as plt

# Definition of data points - as much data points as possible from the table
years = ['2016', '2017', '2018', '2019', '2020']
coal = [30, 28, 25, 23, 22]
natural_gas = [34, 35, 36, 37, 34]
renewables = [20, 22, 24, 26, 28]
nuclear = [12, 12, 11, 10, 12]
oil = [4, 3, 4, 4, 4]

# Colors for the data series for better clarity
colors = ['#4CAF50', '#FFC107', '#2196F3', '#9C27B0', '#FF5722']

# Create a figure and a set of subplots - modify width and height of the chart
fig, ax = plt.subplots(figsize=(12, 7))

# Change the width of bars (here it's the height because this is a horizontal bar chart)
bar_height = 0.6

# Stacking bars vertically
ax.bar(years, coal, color=colors[0], edgecolor='white', width=bar_height, label='Coal')
ax.bar(years, natural_gas, bottom=coal, color=colors[1], edgecolor='white', width=bar_height, label='Natural Gas')
ax.bar(years, renewables, bottom=[i+j for i,j in zip(coal, natural_gas)], color=colors[2], edgecolor='white', width=bar_height, label='Renewables')
ax.bar(years, nuclear, bottom=[i+j+k for i,j,k in zip(coal, natural_gas, renewables)], color=colors[3], edgecolor='white', width=bar_height, label='Nuclear')
ax.bar(years, oil, bottom=[i+j+k+l for i,j,k,l in zip(coal, natural_gas, renewables, nuclear)], color=colors[4], edgecolor='white', width=bar_height, label='Oil')

# Labeling the chart
ax.set_ylabel('Year')
ax.set_xlabel('Percentage (%)')
ax.set_title('Energy Consumption by Source (2016-2020)', pad=20)

# Displaying the legend
ax.legend()

# Adding numerical labels
for i in range(len(years)):
    ax.text(i, coal[i]/2, str(coal[i]), ha='center', va='center', color='white')
    ax.text(i, coal[i] + natural_gas[i]/2, str(natural_gas[i]), ha='center', va='center', color='white')
    ax.text(i, coal[i] + natural_gas[i] + renewables[i]/2, str(renewables[i]), ha='center', va='center', color='white')
    ax.text(i, coal[i] + natural_gas[i] + renewables[i] + nuclear[i]/2, str(nuclear[i]), ha='center', va='center', color='white')
    ax.text(i, coal[i] + natural_gas[i] + renewables[i] + nuclear[i] + oil[i]/2, str(oil[i]), ha='center', va='center', color='white')

# Show the plot
plt.tight_layout()
plt.show()