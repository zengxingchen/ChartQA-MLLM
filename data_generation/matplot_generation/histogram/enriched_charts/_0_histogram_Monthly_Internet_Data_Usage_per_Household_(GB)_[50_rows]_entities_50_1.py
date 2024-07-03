
import matplotlib.pyplot as plt

# Data: ages of participants at an event
ages = [23, 26, 29, 22, 21, 35, 37, 30, 20, 25, 28, 29, 36, 38, 27, 31, 34, 22, 21, 24, 23, 18, 19, 32, 33, 39, 
        24, 36, 31, 25, 23, 27, 33, 35, 30, 22, 25, 28, 30, 31, 35, 36, 39, 40, 19, 20, 21, 25, 26, 27, 29, 30, 
        32, 34, 36, 37, 38, 40, 21, 22, 23, 25, 25, 28, 29, 30, 31, 33, 35, 37, 39, 20, 22, 24, 26, 27, 29, 30, 
        32, 33, 35, 36, 38, 39, 41, 42, 43, 45]

# Set the size of the figure
plt.figure(figsize=(8, 6))

# Create histogram with specified bins, orientation, color, and width of the bars
plt.hist(ages, bins=10, orientation='horizontal', color='#6A0DAD', rwidth=0.9)  # Purple color

# Set the title and labels
plt.title('Age Distribution of Event Participants')
plt.xlabel('Number of Participants')
plt.ylabel('Ages')

# Show the plot
plt.show()