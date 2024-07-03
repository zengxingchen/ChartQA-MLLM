
import matplotlib.pyplot as plt

# Data to plot
labels = 'Fruits', 'Vegetables', 'Proteins', 'Carbohydrates', 'Fats'
sizes = [25, 30, 20, 15, 10]
colors = ['#ff6347', '#98fb98', '#ffd700', '#87ceeb', '#ff69b4']

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Daily Nutrient Intake Distribution', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()