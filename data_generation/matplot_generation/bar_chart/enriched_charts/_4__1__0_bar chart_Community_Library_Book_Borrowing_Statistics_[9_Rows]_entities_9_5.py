
import matplotlib.pyplot as plt

# Data
activities = ['Sleep', 'Work', 'Exercise', 'Reading', 'Meditation', 'Cooking', 
              'Family Time', 'Socializing', 'Screen Time', 'Learning', 
              'Hobbies', 'Outdoor Activities']
hours = [7.5, 8, 1.5, 2, 0.5, 1, 2.5, 1.5, 3, 1, 1.5, 1]

# Create horizontal bar chart
plt.figure(figsize=(12, 8))  # Width, Height of the chart
plt.barh(activities, hours, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
                                   '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#9edae5', '#ff9896'], 
         height=0.5)  # Height of the bars

# Set the title and labels
plt.title('Weekly Hours Spent on Health & Psychological Activities', pad=20)
plt.xlabel('Hours per Week')
plt.ylabel('Activity')

# Set y-axis limits to start from a specific value
plt.xlim(0.4, 8.5)

# Show the plot
plt.show()