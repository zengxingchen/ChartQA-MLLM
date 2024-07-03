
import matplotlib.pyplot as plt

# Data
topics = [
    'Literature', 'Science', 'History', 'Art', 'Music', 
    'Technology', 'Philosophy', 'Economics', 'Psychology', 
    'Education', 'Politics', 'Environment', 'Adventure', 
    'Sports'
]
counts = [70, 45, 55, 25, 40, 65, 30, 50, 35, 60, 38, 48, 28, 52]
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33FF', '#FFFF33', 
    '#33FFF7', '#5733FF', '#FF3380', '#FF8C00', '#FF6347', 
    '#32CD32', '#FFD700', '#C71585', '#1E90FF'
]

# Create a pie chart
plt.figure(figsize=(12, 9))  # Adjusting the size of the pie chart
plt.pie(counts, labels=topics, colors=colors, startangle=100, autopct='%1.1f%%')

# Title of the pie chart
plt.title('Interest Distribution by Topic in Humanities and Sciences', pad=20)

plt.show()