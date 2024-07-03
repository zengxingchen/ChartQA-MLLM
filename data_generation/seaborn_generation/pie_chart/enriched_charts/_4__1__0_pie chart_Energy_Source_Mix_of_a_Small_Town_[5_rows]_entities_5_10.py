
import matplotlib.pyplot as plt

labels = 'Running', 'Cycling', 'Swimming', 'Yoga', 'Weightlifting'
sizes = [300, 250, 200, 150, 100]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

plt.figure(figsize=(12,9))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Popular Sports Activities', pad=20)
plt.axis('equal')  
plt.show()