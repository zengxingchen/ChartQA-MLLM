
import matplotlib.pyplot as plt

# Data points
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
visitors = [3.2, 3.5, 3.9, 4.0, 4.3, 4.6, 4.2, 4.8, 5.1, 4.9, 5.3, 5.6, 5.8]

# Create figure and plot
fig, ax = plt.subplots(figsize=(14, 7))  # Change width and height of the chart

# Change the color scheme using specific hex codes
ax.plot(years, visitors, color='#ff5733', marker='D')  # Example color code and marker for each point

# Set the title and labels
ax.set_title('Annual Visitor Statistics', fontsize=16)  # Change the topic and headline of the chart
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Visitors (Millions)', fontsize=14)

# Adding annotations/labels
for (year, visitor) in zip(years, visitors):
    ax.annotate(f'{visitor}', xy=(year, visitor), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)  # Adding grid
plt.show()