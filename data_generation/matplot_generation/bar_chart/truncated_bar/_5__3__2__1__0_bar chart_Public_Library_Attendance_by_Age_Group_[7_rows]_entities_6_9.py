
import matplotlib.pyplot as plt

# Data
categories = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
hours = [5, 7, 6, 8, 9, 11, 10, 12, 13, 12, 11, 14]

# Colors for each bar
colors = ['#A83279', '#3E64FF', '#F5D020', '#FF006E', '#8338EC', '#00F5D4', '#4CAF50', '#FF5733', '#C70039', '#900C3F', '#581845', '#1ABC9C']

# Create a horizontal bar chart
plt.figure(figsize=(10, 8))  # Change the figure size (width x height)
bar_height = 0.6  # Change the bar height
plt.barh(categories, hours, color=colors, height=bar_height)

# Setting the title and labels
plt.title('Average Study Hours per Month in 2023', pad=20)
plt.xlabel('Hours')
plt.ylabel('Month')

# Set the y-axis limit to start from 4
plt.xlim([4, max(hours) + 2])

# Display the chart
plt.tight_layout()
plt.show()