
import matplotlib.pyplot as plt
import numpy as np

categories = ['Technology', 'Healthcare', 'Finance', 'Energy']
quarters = ['2021 Q1', '2021 Q2', '2021 Q3', '2021 Q4', '2022 Q1', '2022 Q2', '2022 Q3', '2022 Q4']

data = np.array([
    [15, 20, 25, 30, 35, 40, 45, 50],  # Technology
    [35, 30, 25, 20, 25, 30, 35, 40],  # Healthcare
    [25, 30, 20, 25, 30, 25, 20, 15],  # Finance
    [25, 20, 30, 25, 10, 5, 0, 0],     # Energy
])

data_percentage = data / data.sum(axis=0) * 100

colors = ['#1E90FF', '#32CD32', '#FFD700', '#FF4500']

fig, ax = plt.subplots(figsize=(10, 12))
width = 0.5

for i in range(len(categories)):
    bottom = np.sum(data_percentage[:i], axis=0)
    ax.bar(quarters, data_percentage[i], bottom=bottom, width=width, color=colors[i], label=categories[i])

ax.set_ylabel('Percentage')
ax.set_title('Annual Sector Distribution', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()