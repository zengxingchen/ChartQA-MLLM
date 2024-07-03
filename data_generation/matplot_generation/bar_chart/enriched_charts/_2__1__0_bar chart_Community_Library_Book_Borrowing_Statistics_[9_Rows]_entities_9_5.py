
import matplotlib.pyplot as plt

# Data
activities = ['Physics', 'Chemistry', 'Biology', 'Mathematics', 'Astronomy', 'Geology', 
              'Ecology', 'Computer Science', 'Engineering', 'Statistics', 
              'Quantum Mechanics', 'Genetics']
hours = [8, 5, 7, 6, 4, 3, 2, 9, 5, 7, 4, 6]

# Create horizontal bar chart
plt.figure(figsize=(12, 8))  # Width, Height of the chart
plt.barh(activities, hours, color=['#1E90FF', '#FF6347', '#32CD32', '#FFD700', '#4B0082', 
                                   '#FF4500', '#00FA9A', '#8A2BE2', '#A0522D', '#FF69B4', 
                                   '#7FFF00', '#4682B4'], height=0.5)  # Height of the bars

# Set the title and labels
plt.title('Weekly Study Hours in Various Science Subjects', pad=20)
plt.xlabel('Hours per Week')
plt.ylabel('Subject')

# Show the plot
plt.show()