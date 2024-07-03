
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
exercise = [30000, 32000, 34000, 35000, 36000, 37000, 38000, 39000, 40000, 41000, 42000, 43000]
sleep = [25000, 26000, 27000, 28000, 29000, 30000, 31000, 32000, 33000, 34000, 35000, 36000]
meditation = [20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000, 31000]
healthy_eating = [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000]

fig, ax = plt.subplots(figsize=(12, 6))  # change width and height of the chart

bar_width = 0.35  # change width of bars

# Plotting data (change direction of chart to vertical)
p1 = ax.bar(months, exercise, bar_width, color='#4B8BBE', label='Exercise')
p2 = ax.bar(months, sleep, bar_width, bottom=exercise, color='#306998', label='Sleep')
p3 = ax.bar(months, meditation, bar_width, bottom=[i+j for i,j in zip(exercise, sleep)], color='#FFE873', label='Meditation')
p4 = ax.bar(months, healthy_eating, bar_width, bottom=[i+j+k for i,j,k in zip(exercise, sleep, meditation)], color='#FFD43B', label='Healthy Eating')

ax.set_ylabel('Hours')
ax.set_title('Monthly Health Activities Comparison')
ax.set_xticks([i for i in range(len(months))])
ax.set_xticklabels(months)
ax.legend()

# Customize the grid
plt.grid(which='major', linestyle='--', linewidth='0.5', color='black')

# Add numerical labels
for rects in [p1, p2, p3, p4]:
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, rect.get_y() + height / 2),
                    xytext=(0, 0),
                    textcoords="offset points",
                    ha='center', va='center', fontsize=8)

plt.show()