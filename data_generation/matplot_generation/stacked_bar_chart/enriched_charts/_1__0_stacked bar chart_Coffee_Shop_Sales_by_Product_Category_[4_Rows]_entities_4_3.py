
import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
running = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
swimming = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]
cycling = [60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170]

# Colors
colors_running = '#8e44ad'
colors_swimming = '#2980b9'
colors_cycling = '#27ae60'

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))  # Change the figure size

bar_width = 0.35  # Change the width of the bars

y_positions = range(len(months))
bar_positions_running = [pos - bar_width for pos in y_positions]
bar_positions_swimming = y_positions
bar_positions_cycling = [pos + bar_width for pos in y_positions]

ax.bar(bar_positions_running, running, bar_width, label='Running', color=colors_running)
ax.bar(bar_positions_swimming, swimming, bar_width, bottom=running, label='Swimming', color=colors_swimming)
ax.bar(bar_positions_cycling, cycling, bar_width, bottom=[x + y for x, y in zip(running, swimming)], label='Cycling', color=colors_cycling)

ax.set_ylabel('Participation (in thousands)')
ax.set_title('Monthly Participation in Different Sports Activities Over a Year')
ax.set_xticks(y_positions)
ax.set_xticklabels(months)
ax.legend()

plt.tight_layout()
plt.show()