
import matplotlib.pyplot as plt

# Data
categories = ['Fiction', 'Non-Fiction', 'Science']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
fiction = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
non_fiction = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
science = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]

# Colors
colors_fiction = '#FF6347'
colors_non_fiction = '#4682B4'
colors_science = '#32CD32'

# Plotting
fig, ax = plt.subplots(figsize=(10, 12))  # Change the figure size

bar_height = 0.4  # Change the height of the bars

x_positions = range(len(months))
bar_positions_fiction = [pos - bar_height for pos in x_positions]
bar_positions_non_fiction = x_positions
bar_positions_science = [pos + bar_height for pos in x_positions]

ax.barh(bar_positions_fiction, fiction, bar_height, label='Fiction', color=colors_fiction)
ax.barh(bar_positions_non_fiction, non_fiction, bar_height, left=fiction, label='Non-Fiction', color=colors_non_fiction)
ax.barh(bar_positions_science, science, bar_height, left=[x + y for x, y in zip(fiction, non_fiction)], label='Science', color=colors_science)

ax.set_xlabel('Sales (in thousands)')
ax.set_title('Monthly Book Sales in Different Genres Over a Year', pad=20)
ax.set_yticks(x_positions)
ax.set_yticklabels(months)
ax.legend()

# Add numerical labels
for index, value in enumerate(fiction):
    ax.text(value/2, bar_positions_fiction[index], str(value), ha='center', va='center', color='white')
for index, value in enumerate(non_fiction):
    ax.text(fiction[index] + value/2, bar_positions_non_fiction[index], str(value), ha='center', va='center', color='white')
for index, value in enumerate(science):
    ax.text(fiction[index] + non_fiction[index] + value/2, bar_positions_science[index], str(value), ha='center', va='center', color='white')

plt.tight_layout()
plt.show()