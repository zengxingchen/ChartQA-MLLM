
import matplotlib.pyplot as plt

labels = ['Proteins', 'Fruits', 'Vegetables', 'Dairy', 'Grains', 'Sweets']
sizes = [350, 200, 250, 150, 100, 75]
colors = ['#ff6666', '#66c2ff', '#66ff66', '#ffcc66', '#c2a2f0', '#ffb366']

plt.figure(figsize=(12,8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Daily Food Intake Distribution', pad=20)
plt.axis('equal')
plt.show()