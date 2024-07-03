
import matplotlib.pyplot as plt

# Data
categories = ['Mental Health', 'Nutrition', 'Physical Exercise', 'Sleep Quality', 
              'Stress Management', 'Relationships', 'Substance Abuse', 'Personal Development', 
              'Cognitive Health', 'Sexual Health', 'Work-Life Balance']
percentages = [20.5, 15.0, 25.0, 10.0, 8.0, 7.0, 5.0, 4.5, 5.0, 3.0, 4.0]

# Colors
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', 
          '#FF6666', '#66FF66', '#FF66B2', '#FFB266', '#6666FF', 
          '#FF66FF']

# Pie chart
fig, ax = plt.subplots(figsize=(12, 8))  # Width, Height of the chart
ax.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Health & Psychology Focus Areas', pad=20)
plt.show()