
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Quarter': 'Q1-2019', 'Administration': '15%', 'Sales': '30%', 'Marketing': '20%', 'IT': '10%', 'Operations': '15%', 'Customer Service': '10%'},
    {'Quarter': 'Q2-2019', 'Administration': '14%', 'Sales': '30%', 'Marketing': '21%', 'IT': '11%', 'Operations': '14%', 'Customer Service': '10%'},
    # ... (include all the data points here)
    {'Quarter': 'Q4-2021', 'Administration': '20%', 'Sales': '19%', 'Marketing': '29%', 'IT': '12%', 'Operations': '10%', 'Customer Service': '10%'}
]

# Convert percentages from string to float
for entry in data:
    for key in entry:
        if key != 'Quarter':
            entry[key] = float(entry[key].strip('%'))

# Extract categories and quarters
categories = [key for key in data[0].keys() if key != 'Quarter']
quarters = [entry['Quarter'] for entry in data]

# Prepare data for stacking in the bar chart
stacks = {}
for category in categories:
    stacks[category] = [entry[category] for entry in data]

# Colors to make each stack distinct
colors = plt.cm.get_cmap('tab20', len(categories))

# Plotting the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 7))

bottom_stack = [0] * len(quarters)
for i, category in enumerate(categories):
    ax.bar(quarters, stacks[category], bottom=bottom_stack, color=colors(i), edgecolor='white', label=category)
    # Update bottom stack
    bottom_stack = [bottom_stack[j] + stacks[category][j] for j in range(len(bottom_stack))]

# Formatting the plot
ax.set_title('Department Expenses by Quarter (Percentage Stacked Bar Chart)')
ax.set_xlabel('Quarter')
ax.set_ylabel('Percentage')
plt.xticks(rotation=45)
plt.yticks(range(0, 101, 10))  # Setting y-ticks to show percentage scale

# Adding a legend
ax.legend(title='Departments', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the values on the bars
for i in range(len(quarters)):
    cumulative_height = 0
    for category in categories:
        height = stacks[category][i]
        if height > 0:  # Only show label if height (percentage) is greater than 0
            ax.text(i, cumulative_height + height/2, f'{height}%', ha='center', va='center', fontsize=8)
        cumulative_height += height

# Show the plot
plt.tight_layout()
plt.show()