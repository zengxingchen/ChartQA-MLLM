
import matplotlib.pyplot as plt
import numpy as np

categories = [
    'Technology', 'Healthcare', 'Finance', 'Retail', 'Energy', 'Real Estate',
    'Telecom', 'Automobile', 'Pharmaceuticals', 'Food & Beverage', 'Education',
    'Hospitality', 'Media', 'Transport', 'Aerospace', 'Agriculture', 'Mining',
    'Logistics', 'Construction', 'Fashion'
]
investment = np.array([500, 600, 450, 550, 400, 700, 350, 300, 800, 450, 500, 600, 550, 400, 700, 650, 300, 500, 600, 450])
revenue = np.array([1500, 1300, 1200, 1400, 1100, 1600, 1000, 900, 1700, 1150, 1300, 1450, 1250, 1050, 1550, 1350, 950, 1400, 1200, 1100])
roi = np.array([200, 150, 167, 155, 175, 129, 186, 200, 113, 156, 160, 142, 127, 163, 121, 107, 217, 180, 100, 144])

sizes = investment * 2

colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFA6',
    '#FFC733', '#337BFF', '#FF337B', '#7BFF33', '#33FFD5', '#FF8633',
    '#33FFDA', '#FF33D5', '#A6FF33', '#33B3FF', '#FF333A', '#FF8333',
    '#33FF95', '#FFAC33'
]

plt.figure(figsize=(20, 12))

scatter = plt.scatter(investment, revenue, s=sizes, c=colors, alpha=0.7, edgecolors="k", linewidth=1.5)

plt.title('Investment vs Revenue Across Industries', pad=30)
plt.xlabel('Investment (Million USD)')
plt.ylabel('Revenue (Million USD)')

for i, category in enumerate(categories):
    plt.annotate(category, (investment[i], revenue[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()