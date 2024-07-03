
import matplotlib.pyplot as plt

# Data to plot
labels = ['Fruit', 'Vegetables', 'Grains', 'Protein', 'Dairy', 'Snacks', 'Beverages']
sizes = [100, 150, 200, 120, 90, 130, 110]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#A833FF', '#FFA833', '#33FFA8']

# Plot
plt.figure(figsize=(14, 10))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Food & Nutrition Distribution in 2023', y=1.05)
plt.axis('equal')
plt.show()