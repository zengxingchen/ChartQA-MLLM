
import matplotlib.pyplot as plt

# Data: duration of exercise sessions in minutes
duration = [12, 15, 17, 14, 18, 19, 22, 20, 23, 21, 24, 19, 17, 16, 15, 22, 25, 26, 28, 19, 30, 32, 34, 33, 35, 29, 
            31, 27, 18, 25, 20, 22, 19, 21, 23, 26, 27, 30, 32, 29, 34, 31, 33, 25, 36, 38, 40, 37, 39, 41, 35, 28, 
            30, 27, 26, 24, 29, 33, 34, 38, 39, 41, 28, 29, 31, 35, 37, 38, 40, 39, 30, 33, 34, 31, 29, 32, 35, 36, 
            38, 41, 43, 45, 47, 46, 42, 44, 43, 45, 39, 40, 42, 44, 46, 48, 49, 50, 47, 45, 44, 43, 42, 40, 38, 37, 
            36, 39, 41, 43, 45, 47, 48, 49, 50]

# Set the size of the figure
plt.figure(figsize=(10, 8))

# Create histogram with specified bins, orientation, color, and width of the bars
plt.hist(duration, bins=12, orientation='vertical', color='#FFA500', rwidth=0.8)  # Orange color

# Set the title and labels
plt.title('Duration of Exercise Sessions')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Sessions')

# Show the plot
plt.show()