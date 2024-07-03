
import matplotlib.pyplot as plt

# Data points
temperatures = [
    22, 23, 22, 21, 20, 19, 24, 25, 23, 26, 28, 30, 27, 26, 29, 21, 22, 20, 19, 18,
    17, 16, 23, 24, 21, 19, 25, 26, 28, 29, 23, 22, 24, 25, 26, 21, 20, 19, 23, 25,
    27, 28, 30, 31, 29, 28, 27, 26, 24, 23, 22
]

# Modify the color scheme using specific color codes for better clarity or visual appeal.
colors = '#6baed6'

# Change width of histograms reasonably (not too narrow or wide)
bin_width = 1

# Change width and height of the chart reasonably
plt.figure(figsize=(12, 6))

# Change the direction of chart (vertical to horizontal)
plt.hist(temperatures, bins=range(int(min(temperatures)), int(max(temperatures)) + bin_width, bin_width), color=colors, orientation='horizontal')

# Change the band width/height for histograms (bin width has been set to 1 above)
plt.xlabel('Frequency')
plt.ylabel('Temperature (°C)')

# Change the topic, headline, and data type (which fit the topic) of the chart
plt.title('Frequency Distribution of Daily Temperatures Over a Month')
plt.grid(True)

plt.show()