
import matplotlib.pyplot as plt

# Define the data points
years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
population_growth = [2.1, 2.5, 2.3, 2.7, 2.4, 2.6, 2.9, 3.1, 3.0, 3.2, 3.5, 3.7, 3.9]

# Create the line chart
plt.figure(figsize=(10, 5)) # Changed width and height of the chart
plt.plot(years, population_growth, color='#FF4500', marker='o') # Changed color scheme and added markers

# Modify the data points to introduce a dip in 2014
population_growth[4] = 2.0
plt.plot(years, population_growth, linestyle='--', color='#1E90FF') # Overlaying the modified trend line

# Assign annotation to the chart
for i, pop in enumerate(population_growth):
    plt.annotate(f"{pop}%", (years[i], population_growth[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Axes and title
plt.title('Population Growth Rate (2010-2022)', pad=20)
plt.xlabel('Year')
plt.ylabel('Growth Rate (%)')
plt.grid(True)

# Display the plot
plt.show()