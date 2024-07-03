
import matplotlib.pyplot as plt

# Data to plot
labels = 'Ancient Civilizations', 'Medieval Period', 'Renaissance', 'Industrial Revolution', 'Modern Era'
sizes = [320, 250, 180, 210, 140]
colors = ['#FF9999', '#66B2FF', '#FFCC99', '#99FF99', '#FF9966']

# Plot
plt.figure(figsize=(12, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Historical Eras and Their Significance', y=1.08)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()