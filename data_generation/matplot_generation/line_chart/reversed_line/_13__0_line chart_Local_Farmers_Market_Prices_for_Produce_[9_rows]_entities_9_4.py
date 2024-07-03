
import matplotlib.pyplot as plt

# Data points
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
gdp_growth = [2.563, 1.550, 2.249, 1.842, 1.500, 2.908, 1.637, 2.369, 2.927, 3.500, -3.517, 5.973, 2.845]

# Create figure and plot
fig, ax = plt.subplots(figsize=(12, 6))  # Change width and height of the chart

# Change the color scheme using specific hex codes
ax.plot(years, gdp_growth, color='#1F77B4', marker='o')  # Example color code and marker for each point

# Set the title and labels
ax.set_title('Annual Rainfall Variation', fontsize=16)  # Change the topic and headline of the chart
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Rainfall Variation (%)', fontsize=14)
ax.invert_yaxis()  # Invert the y-axis

# Adding annotations/labels
for (year, growth) in zip(years, gdp_growth):
    ax.annotate(f'{growth}%', xy=(year, growth), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)  # Adding grid
plt.show()