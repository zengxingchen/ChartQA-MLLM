
import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
phones = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]
laptops = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
tablets = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

# Colors
colors_phones = '#1f77b4'
colors_laptops = '#ff7f0e'
colors_tablets = '#2ca02c'

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))  # Change the figure size

bar_width = 0.4  # Change the width of the bars

x_positions = range(len(months))
bar_positions_phones = [pos - bar_width for pos in x_positions]
bar_positions_laptops = x_positions
bar_positions_tablets = [pos + bar_width for pos in x_positions]

ax.bar(bar_positions_phones, phones, bar_width, label='Phones', color=colors_phones)
ax.bar(bar_positions_laptops, laptops, bar_width, bottom=phones, label='Laptops', color=colors_laptops)
ax.bar(bar_positions_tablets, tablets, bar_width, bottom=[x + y for x, y in zip(phones, laptops)], label='Tablets', color=colors_tablets)

ax.set_ylabel('Sales (in thousands)')
ax.set_title('Monthly Sales of Different Electronic Products in 2023', pad=20)
ax.set_xticks(x_positions)
ax.set_xticklabels(months)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Add numerical labels
for index, value in enumerate(phones):
    ax.text(bar_positions_phones[index], value / 2, str(value), ha='center', va='center', color='white')
for index, value in enumerate(laptops):
    ax.text(bar_positions_laptops[index], phones[index] + value / 2, str(value), ha='center', va='center', color='white')
for index, value in enumerate(tablets):
    ax.text(bar_positions_tablets[index], phones[index] + laptops[index] + value / 2, str(value), ha='center', va='center', color='white')

plt.tight_layout()
plt.show()