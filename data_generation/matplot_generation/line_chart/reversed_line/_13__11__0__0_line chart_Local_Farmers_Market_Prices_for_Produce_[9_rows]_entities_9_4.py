
import matplotlib.pyplot as plt

# Data points
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
visitors = [5.8, 5.6, 5.9, 6.0, 5.7, 6.2, 5.5, 6.3, 5.1, 6.5, 5.4, 6.6, 5.3]

# Create figure and plot
fig, ax = plt.subplots(figsize=(12, 8))

# Change the color scheme using specific hex codes
ax.plot(years, visitors, color='#3399ff', marker='o')  # Example color code and marker for each point

# Set the title and labels
ax.set_title('Annual Sports Event Attendance', fontsize=18, pad=20)  # Change the topic and headline of the chart
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Attendees (Millions)', fontsize=14)

# Adding annotations/labels
for (year, visitor) in zip(years, visitors):
    ax.annotate(f'{visitor}', xy=(year, visitor), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)  # Adding grid
plt.show()