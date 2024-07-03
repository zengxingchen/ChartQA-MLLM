
import matplotlib.pyplot as plt

# Data points
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
life_expectancy = [70.8, 71.2, 71.5, 71.9, 72.3, 72.7, 73.1, 73.4, 73.8, 74.1, 74.5, 74.8, 75.2]

# Create figure and plot
fig, ax = plt.subplots(figsize=(12, 6))  # Change width and height of the chart

# Change the color scheme using specific hex codes
ax.plot(years, life_expectancy, color='#1f77b4', marker='o')  # Example color code and marker for each point

# Set the title and labels
ax.set_title('Annual Life Expectancy', fontsize=16)  # Change the topic and headline of the chart
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Life Expectancy (Years)', fontsize=14)

# Adding annotations/labels
for (year, le) in zip(years, life_expectancy):
    ax.annotate(f'{le}', xy=(year, le), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)  # Adding grid
plt.show()