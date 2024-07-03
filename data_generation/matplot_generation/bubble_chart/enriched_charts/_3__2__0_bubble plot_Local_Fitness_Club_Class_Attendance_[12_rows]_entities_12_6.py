
import matplotlib.pyplot as plt

age_groups = ['10-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100', '101-110', '111-120', '121-130']
participants = [8.5, 7.8, 6.9, 6.0, 5.5, 4.8, 4.2, 3.5, 2.8, 2.1, 1.5, 1.0]
satisfaction_scores = [7.0, 6.5, 5.8, 5.0, 4.7, 4.2, 3.8, 3.0, 2.5, 2.0, 1.5, 1.2]
population = [1700, 2200, 2100, 1800, 1600, 1400, 1200, 1000, 800, 600, 400, 200]
colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF', '#9EDAE5', '#DBDB8D']
sizes = [i / 10 for i in population]

fig, ax = plt.subplots(figsize=(14, 8))

for i in range(len(age_groups)):
    ax.scatter(age_groups[i], participants[i], s=sizes[i], alpha=0.6, color=colors[i])

ax.set_title('Participant Satisfaction Scores by Age Group', pad=20)
ax.set_xlabel('Age Group')
ax.set_ylabel('Satisfaction Score')

plt.show()