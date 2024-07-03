
import matplotlib.pyplot as plt

# Data to plot
labels = 'Cognitive Behavioral Therapy', 'Psychodynamic Therapy', 'Humanistic Therapy', 'Integrative Therapy', 'Art Therapy'
sizes = [30.0, 25.0, 20.0, 15.0, 10.0]
colors = ['#ff6347','#4682b4','#8a2be2','#3cb371','#ffd700']

# Create pie chart
plt.figure(figsize=(12, 9))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Therapy Session Types in 2023', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()