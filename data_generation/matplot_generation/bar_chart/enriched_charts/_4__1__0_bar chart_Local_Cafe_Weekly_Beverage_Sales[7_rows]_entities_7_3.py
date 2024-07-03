
import matplotlib.pyplot as plt

age_groups = ['10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']
average_exercise_hours = [5, 7, 6, 5.5, 4, 3.5, 2, 1.5]

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFBD33', '#33FFF3', '#5733FF', '#FF5733']

plt.figure(figsize=(14, 8))
plt.barh(age_groups, average_exercise_hours, color=colors, edgecolor='black', height=0.6)

plt.xlabel('Average Weekly Exercise Hours', fontsize=12)
plt.ylabel('Age Group', fontsize=12)
plt.title('Average Weekly Exercise Hours by Age Group', fontsize=16, pad=20)
plt.xlim(0, 8)

plt.tight_layout()
plt.show()