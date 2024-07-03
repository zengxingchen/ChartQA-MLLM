import matplotlib.pyplot as plt

# Data points
scores = [
    78, 85, 92, 88, 91, 76, 82, 79, 95, 94, 89, 90, 86, 87, 83, 84, 80, 81, 77, 75,
    74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55,
    54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35,
    34, 33, 32, 31, 30
]

# Modify the color scheme using specific color codes for better clarity or visual appeal.
colors = '#ff7f0e'

# Change width of histograms reasonably
bin_width = 5

# Change width and height of the chart reasonably
plt.figure(figsize=(10, 8))

# Change the direction of chart (horizontal to vertical)
plt.hist(scores, bins=range(int(min(scores)), int(max(scores)) + bin_width, bin_width), color=colors, orientation='vertical')

# Change the band width/height for histograms (bin width has been set to 5 above)
plt.xlabel('Scores')
plt.ylabel('Frequency')

# Change the topic, headline, and data type (which fit the topic) of the chart
plt.title('Distribution of Exam Scores')
plt.grid(True)

plt.show()