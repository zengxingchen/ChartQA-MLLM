
import matplotlib.pyplot as plt

# Data points
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
visitors = [4.4, 4.1, 3.9, 3.8, 3.5, 3.3, 3.1, 2.9, 2.7, 2.5, 2.2, 2.0, 1.8]

# Create figure and plot
fig, ax = plt.subplots(figsize=(10, 6))  # Change width and height of the chart

# Change the color scheme using specific hex codes
ax.plot(years, visitors, color='#ff5733', marker='o')  # Example color code and marker for each point

# Set the title and labels
ax.set_title('Annual Decline in Museum Visitors', fontsize=18, pad=20)  # Change the topic and headline of the chart
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Visitors (Millions)', fontsize=14)

# Adding annotations/labels
for (year, visitor) in zip(years, visitors):
    ax.annotate(f'{visitor}', xy=(year, visitor), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)  # Adding grid
ax.invert_yaxis()  # Inverting y axis
plt.show()