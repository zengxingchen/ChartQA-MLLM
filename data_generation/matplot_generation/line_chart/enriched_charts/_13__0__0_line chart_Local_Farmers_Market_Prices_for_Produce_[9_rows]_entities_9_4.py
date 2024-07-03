
import matplotlib.pyplot as plt

# Data points
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
life_expectancy = [75.2, 74.8, 74.5, 74.1, 73.8, 73.4, 73.1, 72.7, 72.3, 71.9, 71.5, 71.2, 70.8]

# Create figure and plot
fig, ax = plt.subplots(figsize=(10, 5))  # Change width and height of the chart

# Change the color scheme using specific hex codes
ax.plot(years, life_expectancy, color='#ff5733', marker='o')  # Example color code and marker for each point

# Set the title and labels
ax.set_title('Annual Life Expectancy (Inverted Y-Axis)', fontsize=16)  # Change the topic and headline of the chart
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Life Expectancy (Years)', fontsize=14)
ax.invert_yaxis()  # Invert the y-axis

# Adding annotations/labels
for (year, le) in zip(years, life_expectancy):
    ax.annotate(f'{le}', xy=(year, le), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)  # Adding grid
plt.show()