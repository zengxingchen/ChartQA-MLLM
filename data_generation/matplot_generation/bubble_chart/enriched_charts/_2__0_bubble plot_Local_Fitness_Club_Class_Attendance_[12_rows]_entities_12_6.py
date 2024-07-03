
import matplotlib.pyplot as plt

age_groups = ['10-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']
participants = [8.5, 7.8, 6.9, 6.0, 5.5, 4.8, 4.2, 3.5, 2.8]
satisfaction_scores = [7.0, 6.5, 5.8, 5.0, 4.7, 4.2, 3.8, 3.0, 2.5]
population = [1700, 2200, 2100, 1800, 1600, 1400, 1200, 1000, 800]
colors = ['#FF6347', '#FFA07A', '#FFD700', '#ADFF2F', '#32CD32', '#4682B4', '#6A5ACD', '#DA70D6', '#FF69B4']
sizes = [i / 10 for i in population]

fig, ax = plt.subplots(figsize=(12, 7))

for i in range(len(age_groups)):
    ax.scatter(age_groups[i], participants[i], s=sizes[i], alpha=0.6, color=colors[i])

ax.set_title('Participant Satisfaction Scores by Age Group', pad=20)
ax.set_xlabel('Age Group')
ax.set_ylabel('Satisfaction Score')

plt.show()