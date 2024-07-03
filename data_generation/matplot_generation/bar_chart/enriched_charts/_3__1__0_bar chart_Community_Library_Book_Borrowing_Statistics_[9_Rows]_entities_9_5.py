
import matplotlib.pyplot as plt

# Data
activities = ['Abstract Painting', 'Graphic Design', 'Sculpting', 'Digital Art', 'Photography', 'Art Exhibitions',
              'Fashion Design', 'Interior Design', 'Animation', 'Ceramics', 'Calligraphy', 'Street Art']
hours = [8, 7, 5, 10, 6, 4, 7, 3, 9, 5, 6, 4]

# Create horizontal bar chart
plt.figure(figsize=(12, 8))  # Width, Height of the chart
plt.barh(activities, hours, color=['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#33FFF6', '#FFA533',
                                   '#D433FF', '#FFD433', '#33FF9F', '#FF3333', '#33A6FF', '#A6FF33'],
         height=0.5)  # Height of the bars

# Set the title and labels
plt.title('Weekly Hours Spent on Art & Design Activities')
plt.xlabel('Hours per Week')
plt.ylabel('Activity')

# Show the plot
plt.show()