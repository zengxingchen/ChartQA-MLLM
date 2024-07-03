
import matplotlib.pyplot as plt

# Data points
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
values = [75.2, 70.1, 68.3, 65.5, 72.4, 66.7, 61.9, 63.2, 58.4, 64.9, 50.3, 55.6, 49.8]

# Create figure and plot
fig, ax = plt.subplots(figsize=(12, 6))

# Change the color scheme using specific hex codes
ax.plot(years, values, color='#007ACC', marker='x')  # Example color code and marker for each point

# Set the title and labels
ax.set_title('Annual Rainfall in City X', fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Rainfall (cm)', fontsize=14)

# Adding annotations/labels
for (year, value) in zip(years, values):
    ax.annotate(f'{value} cm', xy=(year, value), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)

# Invert y-axis
ax.invert_yaxis()

plt.show()