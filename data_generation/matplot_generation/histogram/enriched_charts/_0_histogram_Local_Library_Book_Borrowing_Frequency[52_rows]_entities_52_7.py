
import matplotlib.pyplot as plt

# Data representing heights of individuals
heights = [
    150, 152, 155, 157, 160, 162, 165, 167, 170, 172, 175, 177, 180, 182,
    185, 187, 190, 192, 195, 197, 200, 202, 205, 207, 210, 212, 215, 217,
    220, 222, 225, 227, 230, 232, 235, 237, 240, 242, 245, 247, 250, 252,
    255, 257, 260, 262, 265, 267, 270, 272, 275, 277, 280, 282, 285, 287,
    290, 292, 295, 297, 300, 302, 305, 307
]

# Set figure size
plt.figure(figsize=(12, 8))

# Create a horizontal histogram with modified color and bin width
plt.hist(heights, bins=30, color='#6A5ACD', orientation='horizontal')

# Set the chart title and labels
plt.title('Distribution of Heights in a Population Sample')
plt.xlabel('Frequency')
plt.ylabel('Height (cm)')

# Customize the tick marks
plt.xticks(range(0, 15, 2))
plt.yticks(range(150, 310, 10))

# Adjust the width of the histogram bars
plt.bar_width = 0.8

# Display the plot
plt.show()