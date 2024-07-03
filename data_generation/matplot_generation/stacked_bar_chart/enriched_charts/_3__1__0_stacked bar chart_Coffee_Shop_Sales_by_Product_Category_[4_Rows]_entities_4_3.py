
import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
running = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]
swimming = [70, 80, 90, 95, 100, 110, 120, 130, 140, 150, 160, 170]
cycling = [90, 100, 110, 115, 120, 130, 140, 150, 160, 170, 180, 190]

# Colors
colors_running = '#FF5733'
colors_swimming = '#33FF57'
colors_cycling = '#3357FF'

# Plotting
fig, ax = plt.subplots(figsize=(10, 14))  # Change the figure size

bar_height = 0.4  # Change the width of the bars

x_positions = range(len(months))
bar_positions_running = [pos - bar_height for pos in x_positions]
bar_positions_swimming = x_positions
bar_positions_cycling = [pos + bar_height for pos in x_positions]

ax.barh(bar_positions_running, running, bar_height, label='Running', color=colors_running)
ax.barh(bar_positions_swimming, swimming, bar_height, left=running, label='Swimming', color=colors_swimming)
ax.barh(bar_positions_cycling, cycling, bar_height, left=[x + y for x, y in zip(running, swimming)], label='Cycling', color=colors_cycling)

ax.set_xlabel('Participation (in thousands)')
ax.set_title('Monthly Participation in Different Fitness Activities Over a Year')
ax.set_yticks(x_positions)
ax.set_yticklabels(months)
ax.legend(loc='lower right')

for i in range(len(months)):
    ax.text(running[i]/2, bar_positions_running[i], str(running[i]), va='center', ha='center', color='white')
    ax.text(running[i] + swimming[i]/2, bar_positions_swimming[i], str(swimming[i]), va='center', ha='center', color='white')
    ax.text(running[i] + swimming[i] + cycling[i]/2, bar_positions_cycling[i], str(cycling[i]), va='center', ha='center', color='white')

plt.tight_layout()
plt.show()