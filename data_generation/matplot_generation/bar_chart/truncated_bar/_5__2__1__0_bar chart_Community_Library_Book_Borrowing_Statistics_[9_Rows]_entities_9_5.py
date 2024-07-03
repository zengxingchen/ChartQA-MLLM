
import matplotlib.pyplot as plt

# Data
categories = ['Stress Management', 'Exercise', 'Nutrition', 'Sleep', 'Meditation', 
              'Work-Life Balance', 'Social Interaction', 'Reading', 'Hobbies', 
              'Therapy', 'Mindfulness', 'Journaling']
hours = [10, 12, 9, 8, 7, 6, 8, 5, 7, 4, 5, 6]

# Create vertical bar chart
plt.figure(figsize=(10, 14))  # Width, Height of the chart
plt.bar(categories, hours, color=['#FF4500', '#1E90FF', '#32CD32', '#FFD700', '#4B0082', 
                                   '#FF6347', '#00FA9A', '#8A2BE2', '#A0522D', '#FF69B4', 
                                   '#7FFF00', '#4682B4'], width=0.6)  # Width of the bars

# Set the title and labels
plt.title('Time Spent on Health & Psychology Activities per Week', pad=20)
plt.ylabel('Hours per Week')
plt.xlabel('Activity')

# Set y-axis limits to truncate the chart
plt.ylim(3, 13)

# Show the plot
plt.show()