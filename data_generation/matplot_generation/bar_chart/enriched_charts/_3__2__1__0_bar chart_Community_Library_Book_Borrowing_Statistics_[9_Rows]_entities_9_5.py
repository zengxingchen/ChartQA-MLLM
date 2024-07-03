
import matplotlib.pyplot as plt

# Data
activities = ['Sleeping', 'Working', 'Eating', 'Exercise', 'Relaxation', 'Socializing', 
              'Commuting', 'Hobbies', 'Housework', 'Childcare', 'Studying', 'Media Consumption']
hours = [8, 9, 2, 1.5, 2, 1, 1.5, 2.5, 1, 1, 1, 3]

# Create vertical bar chart
plt.figure(figsize=(10, 14))  # Width, Height of the chart
plt.bar(activities, hours, color=['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A1', 
                                   '#A133FF', '#33FFA1', '#FFA133', '#FF33FF', '#33A1FF', 
                                   '#A1FF33', '#FF5733'], width=0.5)  # Width of the bars

# Set the title and labels
plt.title('Average Daily Hours Spent on Activities', pad=20)
plt.xlabel('Activity')
plt.ylabel('Hours per Day')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()