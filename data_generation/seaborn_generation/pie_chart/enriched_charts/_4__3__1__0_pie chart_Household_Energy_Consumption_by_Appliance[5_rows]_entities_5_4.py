
import matplotlib.pyplot as plt

# Data to plot
labels = ['Housing', 'Food', 'Transportation', 'Utilities', 'Entertainment', 'Healthcare', 'Savings']
sizes = [35.0, 20.0, 15.0, 10.0, 8.0, 7.0, 5.0]
colors = ['#ff6666', '#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f']

# Create pie chart
plt.figure(figsize=(12, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Monthly Expenses', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()