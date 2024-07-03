
import matplotlib.pyplot as plt

# Data
quarters = ['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 
            'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022',
            'Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023']
healthy_snacks = [50, 60, 55, 65, 70, 75, 80, 85, 90, 95, 100, 105]
processed_foods = [70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
organic_foods = [45, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]

# Colors
colors_healthy = '#3498db'
colors_processed = '#e74c3c'
colors_organic = '#2ecc71'

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))  # Change the figure size

bar_width = 0.4  # Change the width of the bars
bar_spacing = 0.2  # Change the spacing between the bars

y_positions = range(len(quarters))
bar_positions_healthy = [pos - bar_width / 2 - bar_spacing / 2 for pos in y_positions]
bar_positions_processed = y_positions
bar_positions_organic = [pos + bar_width / 2 + bar_spacing / 2 for pos in y_positions]

ax.barh(bar_positions_healthy, healthy_snacks, bar_width, label='Healthy Snacks', color=colors_healthy)
ax.barh(bar_positions_processed, processed_foods, bar_width, left=healthy_snacks, label='Processed Foods', color=colors_processed)
ax.barh(bar_positions_organic, organic_foods, bar_width, left=[x + y for x, y in zip(healthy_snacks, processed_foods)], label='Organic Foods', color=colors_organic)

for i, (h, p, o) in enumerate(zip(healthy_snacks, processed_foods, organic_foods)):
    ax.text(h / 2, bar_positions_healthy[i], str(h), va='center', ha='center', color='white', fontsize=10)
    ax.text(h + p / 2, bar_positions_processed[i], str(p), va='center', ha='center', color='white', fontsize=10)
    ax.text(h + p + o / 2, bar_positions_organic[i], str(o), va='center', ha='center', color='white', fontsize=10)

ax.set_xlabel('Sales (Million Units)')
ax.set_title('Quarterly Sales of Food Categories Over Three Years')
ax.set_yticks(y_positions)
ax.set_yticklabels(quarters)
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()