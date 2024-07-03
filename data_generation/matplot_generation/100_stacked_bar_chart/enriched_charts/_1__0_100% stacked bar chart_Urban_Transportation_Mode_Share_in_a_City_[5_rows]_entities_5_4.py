
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Sleep Quality', 'Physical Activity', 'Diet', 'Mental Health', 'Social Interaction', 'Stress Levels'],
    'Positive': [40, 35, 45, 50, 30, 25],
    'Neutral': [30, 25, 35, 30, 40, 35],
    'Negative': [30, 40, 20, 20, 30, 40]
}

categories = data['Category']
positive = data['Positive']
neutral = data['Neutral']
negative = data['Negative']

bar_width = 0.5
index = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(14, 8))

p1 = ax.barh(index, positive, bar_width, color='#4CAF50')
p2 = ax.barh(index, neutral, bar_width, left=positive, color='#FFC107')
p3 = ax.barh(index, negative, bar_width, left=np.array(positive) + np.array(neutral), color='#F44336')

ax.set_xlabel('Percentage')
ax.set_title('Health & Psychology: Factors Impacting Well-being', pad=20)
ax.set_yticks(index)
ax.set_yticklabels(categories)
ax.legend((p1[0], p2[0], p3[0]), ('Positive', 'Neutral', 'Negative'), loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)

plt.tight_layout()
plt.show()