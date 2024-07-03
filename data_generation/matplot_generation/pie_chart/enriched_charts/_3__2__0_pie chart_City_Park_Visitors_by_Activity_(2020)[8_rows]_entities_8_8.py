
import matplotlib.pyplot as plt

# Data to plot
categories = ['Revenue', 'Expenses', 'Profits', 'Investments', 'Salaries', 'Marketing', 'R&D', 'Operations']
values = [250, 190, 120, 200, 180, 150, 160, 130]
colors = ['#4CAF50', '#2196F3', '#FFC107', '#FF5722', '#9C27B0', '#00BCD4', '#FF9800', '#8BC34A']

# Create pie chart
plt.figure(figsize=(10, 7))
plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Business & Entrepreneurship Budget Allocation for 2023', pad=20)
plt.show()