
import matplotlib.pyplot as plt

# Data points
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
gdp_growth_rate = [3.1, 3.8, 2.5, 3.0, 2.2, 1.9, 1.6, 2.2, 2.9, 2.3, -3.5, 5.7, 2.1]

# Create figure and plot
fig, ax = plt.subplots(figsize=(14, 8))  # Change width and height of the chart

# Change the color scheme using specific hex codes
ax.plot(years, gdp_growth_rate, color='#ff7f0e', marker='s')  # Example color code and marker for each point

# Set the title and labels
ax.set_title('Annual GDP Growth Rate', fontsize=18)  # Change the topic and headline of the chart
ax.set_xlabel('Year', fontsize=16)
ax.set_ylabel('GDP Growth Rate (%)', fontsize=16)

# Adding annotations/labels
for (year, rate) in zip(years, gdp_growth_rate):
    ax.annotate(f'{rate}%', xy=(year, rate), textcoords="offset points", xytext=(0,10), ha='center')

ax.invert_yaxis()  # Invert the y-axis
plt.grid(True)  # Adding grid
plt.show()