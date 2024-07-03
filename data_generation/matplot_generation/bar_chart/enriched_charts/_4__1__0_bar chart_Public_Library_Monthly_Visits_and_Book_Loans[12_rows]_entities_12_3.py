
import matplotlib.pyplot as plt

# Data for the chart
subjects = ['Mathematics', 'Science', 'English', 'History', 'Geography', 
            'Art', 'Music', 'Physical Education', 'Computer Science', 'Economics', 
            'Physics', 'Chemistry', 'Biology', 'Literature', 'Psychology']
hours_studied = [120, 98, 85, 70, 65, 50, 45, 60, 75, 90, 55, 78, 83, 67, 72]

# Setting colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#33FFF1', 
          '#A633FF', '#FFD433', '#FF8333', '#33FFA2', '#FF3366', 
          '#337FFF', '#8D33FF', '#FFBD33', '#33FF8E', '#FF33DC']

# Increase the width and height of the chart
plt.figure(figsize=(14, 8))

# Change the direction of the chart to horizontal and modify the bar width
plt.barh(subjects, hours_studied, color=colors, height=0.6)

# Customizing the chart with titles and labels
plt.xlabel('Hours Studied per Month')
plt.title('Monthly Study Hours per Subject in High School')

# Setting the y-axis limit to truncate the chart
plt.xlim(40, 130)

# Display the bar chart
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()