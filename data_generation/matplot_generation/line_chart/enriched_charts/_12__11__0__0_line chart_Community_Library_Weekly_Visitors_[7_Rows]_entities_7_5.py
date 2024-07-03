
import matplotlib.pyplot as plt

# Define the data points
years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
life_expectancy = [70.1, 70.4, 70.7, 71.0, 71.3, 71.6, 71.9, 72.2, 72.5, 72.8, 72.1, 72.4, 72.7]

# Create the line chart
plt.figure(figsize=(12, 6))
plt.plot(years, life_expectancy, color='#8A2BE2', marker='s')

# Customize the trend of the data by simulating a drop in 2020
life_expectancy[10] = 72.1
plt.plot(years, life_expectancy, linestyle='--', color='#FF4500')

# Assign annotation to the chart
for i, le in enumerate(life_expectancy):
    plt.annotate(f"{le} years", (years[i], life_expectancy[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Axes and title
plt.title('Average Life Expectancy (2010-2022)', pad=20)
plt.xlabel('Year')
plt.ylabel('Life Expectancy (years)')
plt.grid(True)

# Display the plot
plt.show()