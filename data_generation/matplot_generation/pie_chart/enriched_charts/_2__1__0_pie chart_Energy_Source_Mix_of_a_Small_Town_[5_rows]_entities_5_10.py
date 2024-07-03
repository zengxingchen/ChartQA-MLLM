
import matplotlib.pyplot as plt

labels = 'Protein', 'Carbohydrates', 'Fats', 'Vitamins', 'Minerals', 'Fiber'
sizes = [250, 300, 150, 100, 75, 125]
colors = ['#ff6666','#ffcc66','#66ff66','#66b3ff','#c266ff','#ff99cc']

plt.figure(figsize=(12,9))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Nutrient Distribution in a Balanced Diet', pad=20)
plt.axis('equal')  
plt.show()