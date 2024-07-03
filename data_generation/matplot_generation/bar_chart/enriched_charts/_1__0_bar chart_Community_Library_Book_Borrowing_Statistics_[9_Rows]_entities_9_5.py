
import matplotlib.pyplot as plt

# Data
activities = ['Reading', 'Writing', 'Drawing', 'Exercise', 'Music', 'Gaming', 
              'Cooking', 'Travel', 'Photography', 'Gardening', 'Learning', 'Social Media']
hours = [5, 3, 4, 6, 2, 7, 4, 1, 3, 2, 5, 6]

# Create vertical bar chart
plt.figure(figsize=(10, 6))  # Width, Height of the chart
plt.bar(activities, hours, color=['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#4B0082', '#FF4500', 
                                  '#1E90FF', '#8A2BE2', '#00FA9A', '#FF69B4', '#A0522D', '#7FFF00'], 
        width=0.6)  # Width of the bars

# Set the title and labels
plt.title('Weekly Activity Hours')
plt.xlabel('Activity')
plt.ylabel('Hours per Week')

# Show the plot
plt.show()