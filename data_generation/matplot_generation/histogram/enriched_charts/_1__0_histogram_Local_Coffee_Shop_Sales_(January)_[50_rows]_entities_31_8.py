
import matplotlib.pyplot as plt

# Data points
performance_scores = [
    80, 90, 75, 85, 93, 92, 87, 89, 78, 83, 82, 91, 77, 88, 86, 81, 79, 84, 76, 95, 96, 98, 74, 97, 99, 73, 72, 71, 100, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50
]

plt.figure(figsize=(8, 10))  # Change width and height of the chart
n, bins, patches = plt.hist(performance_scores, bins=10, color='#FF5733', rwidth=0.85)  # Changing color and making histogram vertical.

# Setting the colors of individual bars (patches)
for patch in patches:
    patch.set_facecolor('#900C3F')  # A nice maroon color

# Add a black line at the edge of each bar
[patch.set_linewidth(0.5) for patch in patches]
[patch.set_edgecolor('#000000') for patch in patches]

plt.title('Student Performance Scores')
plt.xlabel('Score Range')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()