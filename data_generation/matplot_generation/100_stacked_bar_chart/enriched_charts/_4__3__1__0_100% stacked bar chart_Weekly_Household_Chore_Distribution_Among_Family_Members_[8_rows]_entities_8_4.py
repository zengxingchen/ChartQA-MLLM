
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [15, 30, 35, 20],
    [20, 25, 30, 25],
    [25, 20, 35, 20],
    [30, 25, 20, 25],
    [20, 30, 25, 25],
    [25, 25, 30, 20],
    [30, 20, 25, 25],
    [20, 25, 30, 25],
    [25, 30, 20, 25],
    [30, 20, 25, 25],
    [25, 25, 30, 20],
    [20, 30, 25, 25],
    [25, 20, 35, 20],
    [30, 25, 20, 25],
    [20, 30, 25, 25],
    [25, 25, 30, 20],
    [30, 20, 25, 25],
    [20, 25, 30, 25],
    [25, 30, 20, 25],
    [30, 20, 25, 25]
])

categories = ['Ancient Egypt', 'Medieval Europe', 'Renaissance', 'Industrial Revolution', 'Modern Era', 'Ancient Greece', 
              'Roman Empire', 'Byzantine Empire', 'Ottoman Empire', 'Mesoamerica', 'Indus Valley', 'China Dynasties', 
              'Ancient India', 'Mughal Empire', 'Japanese History', 'Native Americans', 'African Kingdoms', 'Pacific Cultures', 
              'Viking Age', 'Prehistoric Times']
labels = ['History', 'Research', 'Discovery', 'Preservation']
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8']

fig, ax = plt.subplots(figsize=(12, 8))
width = 0.85

bottom = np.zeros(len(data))

for i in range(data.shape[1]):
    ax.bar(categories, data[:, i], width, bottom=bottom, color=colors[i], label=labels[i])
    bottom += data[:, i]

ax.set_xlabel('Historical Periods')
ax.set_ylabel('Percentage')
ax.set_title('Historical Period Contributions')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()