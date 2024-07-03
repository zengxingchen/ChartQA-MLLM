
import matplotlib.pyplot as plt

# Data points
goal_ranges = ["0-1", "2-3", "4-5", "6-7", "8-9", "10-11", "12-13", "14-15", "16-17", "18-19"]
frequency = [2, 5, 9, 13, 8, 7, 4, 3, 2, 1]

# Modify the plot size
plt.figure(figsize=(12, 8))

# Create a horizontal histogram
plt.barh(goal_ranges, frequency, color="#4CAF50", edgecolor="#1B5E20", height=0.7)

# Customize the display
plt.ylabel('Number of Goals Scored', fontsize=12)
plt.xlabel('Frequency', fontsize=12)
plt.title('Distribution of Goals Scored by Players in a Season', fontsize=16)

# Show grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Display the histogram
plt.show()