
import matplotlib.pyplot as plt

# Data
age_groups = ['20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89']
salary_increase_rate = [3.0, 4.1, 3.5, 2.8, 2.2, 1.9, 1.5, 1.2, 1.0, 0.8, 0.6, 0.4, 0.3, 0.2]
population = [2800, 3200, 2900, 2600, 2300, 2000, 1800, 1600, 1400, 1200, 1000, 800, 600, 400]
colors = ['#FF5733', '#FFBD33', '#DBFF33', '#75FF33', '#33FF57', '#33FFBD', '#33DBFF', '#3375FF', '#5733FF', '#BD33FF', '#FF33DB', '#FF3375', '#FF33A8', '#A833FF']
sizes = [i / 10 for i in population]

fig, ax = plt.subplots(figsize=(14, 10))

# Bubble chart
for i in range(len(age_groups)):
    ax.scatter(age_groups[i], salary_increase_rate[i], s=sizes[i], alpha=0.6, color=colors[i], edgecolor='black')

# Title and labels
ax.set_title('Salary Increase Rate by Age Group', pad=20)
ax.set_xlabel('Age Group')
ax.set_ylabel('Salary Increase Rate (%)')

plt.show()