
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Machine Learning', 'Quantum Computing', 'Virtual Reality', 'Cybersecurity', 'Blockchain', 'Biotechnology', 'Renewable Energy', 'Robotics', '3D Printing', 'Nanotechnology'],
    'Positive': [55, 40, 30, 60, 50, 45, 70, 35, 25, 50],
    'Neutral': [25, 35, 40, 20, 30, 25, 15, 40, 45, 25],
    'Negative': [20, 25, 30, 20, 20, 30, 15, 25, 30, 25]
}

categories = data['Category']
positive = data['Positive']
neutral = data['Neutral']
negative = data['Negative']

bar_width = 0.4
index = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(12, 10))

p1 = ax.bar(index, positive, bar_width, color='#1f77b4')
p2 = ax.bar(index, neutral, bar_width, bottom=positive, color='#ff7f0e')
p3 = ax.bar(index, negative, bar_width, bottom=np.array(positive) + np.array(neutral), color='#2ca02c')

ax.set_ylabel('Percentage')
ax.set_title('Future Technologies & Society: Public Perception of Emerging Technologies', pad=20)
ax.set_xticks(index)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.legend((p1[0], p2[0], p3[0]), ('Positive', 'Neutral', 'Negative'), loc='upper right', bbox_to_anchor=(1.2, 1))

plt.tight_layout()
plt.show()