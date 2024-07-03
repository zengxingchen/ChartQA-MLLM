import matplotlib.pyplot as plt

# Data: exercise duration in minutes
exercise_duration = [
    15, 20, 25, 25, 30, 30, 35, 35, 35, 40, 40, 40, 45, 45, 50, 50, 55, 55, 60, 60, 60,
    65, 65, 70, 70, 75, 75, 80, 80, 80, 85, 85, 90, 90, 95, 95, 100, 100, 105, 105, 110,
    110, 115, 115, 120, 120, 125, 125, 130, 130, 135, 135, 140, 140, 145, 145, 150, 150,
    155, 155, 160, 160, 165, 165, 170, 170, 175, 175, 180, 180, 185, 185, 190, 190, 195, 195, 200, 200
]

# Set the size of the histogram
plt.figure(figsize=(8, 12))

# Create a histogram with vertical orientation, modify colors and change bin width
plt.hist(exercise_duration, bins=20, orientation='vertical', color='#1f77b4', rwidth=0.8)

# Add title and labels to xaxis and yaxis
plt.title('Exercise Duration Distribution')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Sessions')

# Show the plot
plt.show()