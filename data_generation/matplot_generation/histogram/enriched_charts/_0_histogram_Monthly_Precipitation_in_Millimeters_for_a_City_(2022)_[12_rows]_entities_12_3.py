
import matplotlib.pyplot as plt

# This is the data for the ages of participants
ages = [
    23, 26, 29, 34, 36, 38, 41, 43, 45, 47, 48, 49, 50, 51, 52, 55, 57, 59, 60, 61, 62,
    65, 68, 70, 72, 74, 75, 76, 78, 80, 82, 85, 87, 89, 91, 93, 95, 97, 99, 100, 101,
    102, 103, 105, 107, 109, 110, 111, 113, 115, 117, 119, 120, 121
]

# Set the size of the figure
plt.figure(figsize=(14, 8))

# Plot the histogram with horizontal orientation, specified bin width, and custom color
plt.hist(ages, bins=range(20, 125, 5), alpha=0.75, orientation='horizontal', color='#6A5ACD')

# Set chart title and labels
plt.title('Age Distribution of Survey Participants')
plt.xlabel('Number of Participants')
plt.ylabel('Age')

# Tweak spacing to prevent clipping of ylabel
plt.tight_layout()

# Show the plot
plt.show()