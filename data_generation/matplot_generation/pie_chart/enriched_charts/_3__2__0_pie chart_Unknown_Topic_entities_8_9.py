
import matplotlib.pyplot as plt

# Data points
categories = ['Reading', 'Writing', 'Editing', 'Researching', 'Reviewing', 'Publishing']
percentages = [25.5, 22.0, 18.0, 15.0, 10.5, 9.0]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFBD33', '#33FFF5']

# Create a pie chart
plt.figure(figsize=(14, 12))
plt.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Distribution of Time Spent on Literary Activities in 2023', pad=40)

# Display the chart
plt.show()