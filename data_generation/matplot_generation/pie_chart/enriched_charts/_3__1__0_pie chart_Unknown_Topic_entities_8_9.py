
import matplotlib.pyplot as plt

# Data points
issues = ['Anxiety', 'Depression', 'Bipolar Disorder', 'Schizophrenia', 'Obsessive-Compulsive Disorder', 'Post-Traumatic Stress Disorder', 'Others']
percentages = [30.0, 25.0, 15.0, 10.0, 8.0, 7.0, 5.0]
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0']

# Create a pie chart
plt.figure(figsize=(10, 7))  # Modify the width and height of the chart
plt.pie(percentages, labels=issues, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Distribution of Mental Health Issues in 2023', pad=20)

# Display the chart
plt.show()