
import matplotlib.pyplot as plt

# Data
activities = ['Research', 'Teaching', 'Consulting', 'Administrative Work', 'Professional Development', 
              'Networking', 'Grading', 'Mentoring', 'Committee Meetings', 'Grant Writing', 
              'Service to Profession', 'Conference Attendance']
hours = [20, 15, 10, 12, 5, 7, 8, 6, 9, 4, 3, 5]

# Create horizontal bar chart
plt.figure(figsize=(14, 10))  # Width, Height of the chart
plt.barh(activities, hours, color=['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#4B0082', 
                                   '#DC143C', '#00CED1', '#FF8C00', '#8A2BE2', '#D2691E', 
                                   '#00FF7F', '#FF1493'], height=0.6)  # Height of the bars

# Set the title and labels
plt.title('Average Weekly Hours Spent on Academic Activities', pad=20)
plt.xlabel('Hours per Week')
plt.ylabel('Activity')

# Set y-axis limits
plt.xlim(0, 25)

# Rotate x-axis labels for better readability
plt.xticks(rotation=0, ha='center')

# Show the plot
plt.tight_layout()
plt.show()