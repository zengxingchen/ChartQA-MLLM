
import matplotlib.pyplot as plt

# Data
categories = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Geography', 'History', 'Languages', 'Arts', 'Other']
percentages = [25.00, 20.00, 15.00, 10.00, 8.00, 7.00, 6.00, 5.00, 4.00, 5.00]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Create a pie chart
plt.figure(figsize=(10, 6))
plt.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)

# Title
plt.title('Popular Subjects in 2023', fontsize=16)

# Display the chart
plt.show()