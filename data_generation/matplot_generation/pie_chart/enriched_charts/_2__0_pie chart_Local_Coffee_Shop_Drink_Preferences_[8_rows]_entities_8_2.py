
import matplotlib.pyplot as plt

labels = 'Apples', 'Bananas', 'Grapes', 'Oranges', 'Cherries', 'Peaches', 'Pineapples', 'Mangoes'
sizes = [150, 90, 80, 60, 50, 40, 30, 20]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#33FFF6', '#F6FF33', '#A633FF', '#FF9633']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Fruits in a Market', pad=20)
plt.axis('equal')
plt.show()