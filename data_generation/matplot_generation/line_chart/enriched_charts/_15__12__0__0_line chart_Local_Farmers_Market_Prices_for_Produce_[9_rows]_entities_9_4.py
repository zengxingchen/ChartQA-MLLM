
import matplotlib.pyplot as plt

# Data points
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
new_song_releases = [50, 45, 60, 55, 65, 70, 75, 80, 85, 90, 100, 110, 105, 120]

# Create figure and plot
fig, ax = plt.subplots(figsize=(16, 10))  # Change width and height of the chart

# Change the color scheme using specific hex codes
ax.plot(years, new_song_releases, color='#1f77b4', marker='x')  # Example color code and marker for each point

# Set the title and labels
ax.set_title('Annual New Song Releases', fontsize=20, pad=25)  # Change the topic and headline of the chart
ax.set_xlabel('Year', fontsize=16)
ax.set_ylabel('Number of Songs', fontsize=16)

# Adding annotations/labels
for (year, n_songs) in zip(years, new_song_releases):
    ax.annotate(f'{n_songs}', xy=(year, n_songs), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)  # Adding grid
plt.gca().invert_yaxis()  # Invert y-axis
plt.show()