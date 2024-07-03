
import matplotlib.pyplot as plt

# Data: scores of students in a class
scores = [85, 88, 90, 87, 86, 95, 92, 85, 82, 84, 87, 91, 93, 90, 89, 84, 81, 82, 88, 86, 85, 83, 94, 95, 90, 
          91, 88, 87, 89, 92, 93, 94, 96, 95, 86, 87, 89, 91, 90, 92, 95, 94, 93, 91, 89, 88, 87, 86, 84, 83, 
          82, 81, 90, 91, 88, 89, 92, 93, 94, 95, 96, 97, 86, 85, 88, 87, 89, 92, 91, 94, 95, 93, 97, 96, 89, 
          90, 92, 91, 94, 93, 88, 87, 86, 85, 84, 83, 82, 81, 90, 91, 94, 93, 92, 95, 96, 97, 89, 88, 85, 84, 
          86, 87, 88, 89]

# Set the size of the figure
plt.figure(figsize=(10, 6))

# Create histogram with specified bins, orientation, color, and width of the bars
plt.hist(scores, bins=15, orientation='vertical', color='#4682B4', rwidth=0.8)  # Steel blue color

# Set the title and labels
plt.title('Score Distribution of Students')
plt.xlabel('Scores')
plt.ylabel('Number of Students')

# Show the plot
plt.show()