
import matplotlib.pyplot as plt

# Data
age_groups = ['20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89']
avg_daily_steps = [8000, 8500, 8200, 7800, 7500, 7200, 6800, 6500, 6200, 5900, 5600, 5300, 5000, 4700]
population = [3000, 3500, 3300, 3100, 2900, 2700, 2500, 2300, 2100, 1900, 1700, 1500, 1300, 1100]
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#00FA9A', '#20B2AA', '#87CEEB', '#4682B4', '#8A2BE2', '#DA70D6', '#FF1493', '#DB7093', '#FF4500', '#FF8C00', '#FFA07A']
sizes = [i / 10 for i in population]

fig, ax = plt.subplots(figsize=(16, 12))

# Bubble chart
for i in range(len(age_groups)):
    ax.scatter(age_groups[i], avg_daily_steps[i], s=sizes[i], alpha=0.6, color=colors[i], edgecolor='black')

# Title and labels
ax.set_title('Average Daily Steps by Age Group', pad=20)
ax.set_xlabel('Age Group')
ax.set_ylabel('Average Daily Steps')

plt.show()