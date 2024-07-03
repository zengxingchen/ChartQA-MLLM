
import matplotlib.pyplot as plt

# Data
topics = [
    'Literature', 'Science', 'History', 'Art', 'Music', 
    'Technology', 'Philosophy', 'Economics', 'Psychology', 
    'Education', 'Politics', 'Environment', 'Adventure', 
    'Sports'
]
counts = [65, 50, 45, 30, 55, 70, 40, 60, 35, 52, 38, 48, 28, 62]
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33FF', '#FFFF33', 
    '#33FFF7', '#5733FF', '#FF3380', '#FF8C00', '#FF6347', 
    '#32CD32', '#FFD700', '#C71585', '#1E90FF'
]

# Create a pie chart
plt.figure(figsize=(14, 10))  # Adjusting the size of the pie chart
plt.pie(counts, labels=topics, colors=colors, startangle=100, autopct='%1.1f%%')

# Title of the pie chart
plt.title('Interest Distribution by Topic in Culture & Society', pad=30)

plt.show()