
import matplotlib.pyplot as plt

# Data points (frequency of occurrences in a dataset)
frequency = [
    18, 23, 45, 38, 47, 12, 22, 33, 42, 41, 56, 39, 23, 28, 47, 32, 38, 53, 43, 29,
    32, 56, 47, 41, 36, 52, 44, 38, 26, 39, 45, 50, 55, 47, 49, 57, 34, 30, 31, 42,
    51, 53, 45, 54, 61, 65, 28, 32
]

# Define the number of bins and their edges
bins = range(0, 70, 10)

# Histogram chart settings
plt.figure(figsize=(10, 6))  # Width and height of the chart
plt.hist(frequency, bins=bins, orientation='vertical', color='#FF6347', rwidth=0.7)

# Titles and labels
plt.title('Distribution of Survey Responses')
plt.xlabel('Frequency of Responses')
plt.ylabel('Number of Occurrences')

# Set limit on vertical axis to enforce uniform bar height
plt.ylim(0, max(frequency) + 5)

# Display the histogram
plt.show()