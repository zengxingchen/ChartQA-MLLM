
import matplotlib.pyplot as plt

# Data to plot
categories = [
    'Nature', 'Science', 'Education', 'Health', 
    'Technology', 'History', 'Entertainment'
]
percentages = [25, 20, 15, 10, 12, 8, 10]

# Define colors for each category
colors = [
    '#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', 
    '#92A8D1', '#955251', '#B565A7'
]

# Creating the pie chart
plt.figure(figsize=(10,8))
plt.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Interest Distribution in Various Fields', pad=20)

plt.show()