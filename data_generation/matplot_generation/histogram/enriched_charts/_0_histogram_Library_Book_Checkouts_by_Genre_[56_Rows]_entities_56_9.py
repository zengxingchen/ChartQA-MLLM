
import matplotlib.pyplot as plt

# Data points (ages of individuals)
ages = [
    7, 13, 22, 23, 25, 30, 31, 35, 35, 37, 40, 41, 44, 45, 45, 46,
    50, 52, 55, 56, 58, 60, 62, 63, 65, 67, 68, 70, 70, 72, 73, 74,
    75, 78, 80, 81, 83, 84, 85, 85, 86, 90, 91, 92, 95, 98
]

# Define the number of bins and their edges
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Histogram chart settings
plt.figure(figsize=(12, 8))  # Width and height of the chart
plt.hist(ages, bins=bins, orientation='horizontal', color='#6A5ACD', rwidth=0.85)

# Titles and labels
plt.title('Age Distribution in a Small Town')
plt.xlabel('Number of People')
plt.ylabel('Ages')

# Set limit on horizontal axis to enforce uniform bar height
plt.xlim(0, max([ages.count(i) for i in range(0, 101)]) + 1)

# Display the histogram
plt.show()