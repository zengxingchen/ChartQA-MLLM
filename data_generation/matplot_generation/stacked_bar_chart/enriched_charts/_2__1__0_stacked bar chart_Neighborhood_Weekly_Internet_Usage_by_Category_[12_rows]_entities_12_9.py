
import matplotlib.pyplot as plt

# Data from the table provided
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
fruits = [50, 55, 60, 65, 70, 75, 80]
vegetables = [60, 65, 70, 75, 80, 85, 90]
grains = [70, 75, 80, 85, 90, 95, 100]
dairy = [80, 85, 90, 95, 100, 105, 110]

# Stacking data
vegetables_bottom = [fruits[i] for i in range(len(fruits))]
grains_bottom = [vegetables_bottom[i] + vegetables[i] for i in range(len(vegetables))]
dairy_bottom = [grains_bottom[i] + grains[i] for i in range(len(grains))]

# Setting figure size
plt.figure(figsize=(10, 12))

# Plotting data
bar_height = 0.8
plt.barh(years, fruits, height=bar_height, color='#ff9999', edgecolor='white', label='Fruits')
plt.barh(years, vegetables, left=vegetables_bottom, height=bar_height, color='#66b3ff', edgecolor='white', label='Vegetables')
plt.barh(years, grains, left=grains_bottom, height=bar_height, color='#99ff99', edgecolor='white', label='Grains')
plt.barh(years, dairy, left=dairy_bottom, height=bar_height, color='#ffcc99', edgecolor='white', label='Dairy')

# Adding titles and labels
plt.xlabel('Consumption in Tons')
plt.ylabel('Year')
plt.title('Annual Food Consumption by Type (2015-2021)')
plt.legend(loc='lower right')

# Adding numerical labels
for i in range(len(years)):
    plt.text(fruits[i] / 2, i, str(fruits[i]), ha='center', va='center', color='black')
    plt.text(vegetables_bottom[i] + vegetables[i] / 2, i, str(vegetables[i]), ha='center', va='center', color='black')
    plt.text(grains_bottom[i] + grains[i] / 2, i, str(grains[i]), ha='center', va='center', color='black')
    plt.text(dairy_bottom[i] + dairy[i] / 2, i, str(dairy[i]), ha='center', va='center', color='black')

# Display the plot
plt.show()