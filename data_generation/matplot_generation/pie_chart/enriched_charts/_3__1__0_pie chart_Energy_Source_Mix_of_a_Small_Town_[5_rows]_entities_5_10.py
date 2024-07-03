
import matplotlib.pyplot as plt

labels = ['Men\'s Wear', 'Women\'s Wear', 'Children\'s Wear', 'Footwear', 'Accessories']
sizes = [200, 300, 150, 120, 80]
colors = ['#ff6666', '#66cc66', '#66b3ff', '#ffcc99', '#c2c2f0']

plt.figure(figsize=(12,9))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Fashion Product Distribution', pad=30)
plt.axis('equal')
plt.show()