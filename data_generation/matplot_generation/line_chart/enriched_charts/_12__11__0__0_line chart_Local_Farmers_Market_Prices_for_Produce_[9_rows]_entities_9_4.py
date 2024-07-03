
import matplotlib.pyplot as plt

# Data points
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
visitors = [1.2, 1.5, 1.8, 2.0, 2.4, 2.7, 2.9, 3.1, 3.5, 3.8, 4.1, 3.9, 4.4]

# Create figure and plot
fig, ax = plt.subplots(figsize=(12, 8))  # Change width and height of the chart

# Change the color scheme using specific hex codes
ax.plot(years, visitors, color='#33aaff', marker='o')  # Example color code and marker for each point

# Set the title and labels
ax.set_title('Annual Museum Visitor Statistics', fontsize=18, pad=20)  # Change the topic and headline of the chart
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Visitors (Millions)', fontsize=14)

# Adding annotations/labels
for (year, visitor) in zip(years, visitors):
    ax.annotate(f'{visitor}', xy=(year, visitor), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)  # Adding grid
plt.show()