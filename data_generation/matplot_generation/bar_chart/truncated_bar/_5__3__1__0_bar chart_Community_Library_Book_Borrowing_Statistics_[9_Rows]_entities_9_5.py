
import matplotlib.pyplot as plt

# Data
activities = ['Reading', 'Writing', 'Editing', 'Research', 'Publishing', 'Proofreading', 'Book Design',
              'Marketing', 'Networking', 'Workshops', 'Conferences', 'Interviews']
hours = [15, 13, 10, 18, 12, 8, 11, 9, 14, 10, 13, 12]

# Create vertical bar chart
plt.figure(figsize=(10, 14))  # Width, Height of the chart
plt.bar(activities, hours, color=['#FF4500', '#1E90FF', '#32CD32', '#FFD700', '#8A2BE2', '#FF6347',
                                  '#4682B4', '#DAA520', '#ADFF2F', '#DC143C', '#8B0000', '#0000CD'],
        width=0.5)  # Width of the bars

# Set the title and labels
plt.title('Weekly Hours Spent on Writing & Publishing Activities', fontsize=16)
plt.xlabel('Activity', fontsize=14)
plt.ylabel('Hours per Week', fontsize=14)

# Set y-axis limits to start from a specific value
plt.ylim(5, 20)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()