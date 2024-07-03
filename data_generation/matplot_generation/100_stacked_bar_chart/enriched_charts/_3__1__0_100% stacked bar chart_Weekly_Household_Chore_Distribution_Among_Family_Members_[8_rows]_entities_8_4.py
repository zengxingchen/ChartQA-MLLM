
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [20, 30, 25, 25],
    [25, 20, 35, 20],
    [30, 25, 20, 25],
    [25, 25, 25, 25],
    [30, 20, 30, 20],
    [20, 30, 25, 25],
    [25, 25, 30, 20],
    [30, 20, 25, 25],
    [25, 25, 20, 30],
    [20, 30, 25, 25],
    [30, 20, 30, 20],
    [25, 25, 25, 25],
    [30, 20, 25, 25],
    [25, 30, 20, 25],
    [20, 30, 25, 25],
    [25, 25, 30, 20],
    [30, 20, 25, 25],
    [25, 25, 20, 30],
    [20, 30, 25, 25],
    [30, 20, 30, 20]
])

categories = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20']
labels = ['Technology', 'Design', 'Marketing', 'Finance']
colors = ['#FF6347', '#4682B4', '#FFD700', '#32CD32']

fig, ax = plt.subplots(figsize=(10, 6))
width = 0.75

bottom = np.zeros(len(data))

for i in range(data.shape[1]):
    ax.bar(categories, data[:, i], width, bottom=bottom, color=colors[i], label=labels[i])
    bottom += data[:, i]

ax.set_xlabel('Quarters')
ax.set_ylabel('Percentage')
ax.set_title('Departmental Contribution Across Quarters')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4)

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()