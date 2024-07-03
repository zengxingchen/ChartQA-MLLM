
import matplotlib.pyplot as plt

age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
drawing = [1.2, 1.0, 0.8, 0.7, 0.5, 0.4]
painting = [0.8, 0.9, 0.7, 0.6, 0.4, 0.3]
sculpting = [0.5, 0.6, 0.7, 0.5, 0.4, 0.3]
photography = [1.0, 1.2, 0.9, 0.8, 0.7, 0.6]

bubble_sizes = [size * 80 for size in drawing + painting + sculpting + photography]

colors = [
    '#FF6347', '#FF4500', '#FF6347', '#FF4500', '#FF6347', '#FF4500',
    '#4682B4', '#5F9EA0', '#4682B4', '#5F9EA0', '#4682B4', '#5F9EA0',
    '#32CD32', '#2E8B57', '#32CD32', '#2E8B57', '#32CD32', '#2E8B57',
    '#FFD700', '#FFA500', '#FFD700', '#FFA500', '#FFD700', '#FFA500'
]

plt.figure(figsize=(12, 8))
plt.scatter(age_groups * 4, drawing + painting + sculpting + photography, s=bubble_sizes, c=colors, alpha=0.6)

plt.title('Average Leisure Hours per Day by Art Activity and Age Group', pad=20)
plt.xlabel('Age Group')
plt.ylabel('Average Hours per Day')

plt.grid(True)

plt.show()