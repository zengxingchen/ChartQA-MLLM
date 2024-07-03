
import matplotlib.pyplot as plt

# Define the data points
years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
gdp_growth = [4.3, 3.0, 2.7, 2.5, 2.8, 2.9, 2.5, 3.2, 3.0, 2.3, -3.4, 6.0, 3.2]

# Create the line chart
plt.figure(figsize=(14, 8)) # Changed width and height of the chart
plt.plot(years, gdp_growth, color='#FF6347', marker='o') # Changed color scheme and added markers

# Customize the trend of the data by simulating a drop in 2020
gdp_growth[10] = -3.4
plt.plot(years, gdp_growth, linestyle='--', color='#4682B4') # Overlaying the modified trend line

# Assign annotation to the chart
for i, gdp in enumerate(gdp_growth):
    plt.annotate(f"{gdp}%", (years[i], gdp_growth[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Axes and title
plt.title('Global GDP Growth (2010-2022)', pad=20)
plt.xlabel('Year')
plt.ylabel('GDP Growth (%)')
plt.grid(True)

# Display the plot
plt.show()