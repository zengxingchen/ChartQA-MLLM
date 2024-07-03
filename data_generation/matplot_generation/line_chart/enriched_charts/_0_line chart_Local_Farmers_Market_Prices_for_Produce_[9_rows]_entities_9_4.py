
import matplotlib.pyplot as plt

# Data points
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
gdp_growth = [2.563, 1.550, 2.249, 1.842, 2.525, 2.908, 1.637, 2.369, 2.927, 2.161, -3.517, 5.973, 2.845]

# Create figure and plot
fig, ax = plt.subplots(figsize=(10, 5))  # change width and height of the chart

# Change the color scheme using specific hex codes
ax.plot(years, gdp_growth, color='#FF5733', marker='o')  # Example color code and marker for each point

# Set the title and labels
ax.set_title('Annual GDP Growth', fontsize=14)  # Change the topic and headline of the chart
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('GDP Growth (%)', fontsize=12)

# Change the trend of data (down/up/cross)
gdp_growth[4] = 1.5  # Changing value at the year 2014
gdp_growth[9] = 3.5  # Changing value at the year 2019

# Adding annotations/labels
for (year, growth) in zip(years, gdp_growth):
    ax.annotate(f'{growth}%', xy=(year, growth), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)  # Adding grid
plt.show()