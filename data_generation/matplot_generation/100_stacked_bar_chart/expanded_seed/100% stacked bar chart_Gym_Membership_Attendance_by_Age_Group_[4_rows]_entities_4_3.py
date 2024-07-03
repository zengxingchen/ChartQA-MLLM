
import matplotlib.pyplot as plt

# Given data
data = [
    {'Age Group': '18-25', 'January': '35%', 'February': '30%', 'March': '38%', 'April': '40%', 'May': '32%'},
    {'Age Group': '26-35', 'January': '25%', 'February': '28%', 'March': '22%', 'April': '20%', 'May': '26%'},
    {'Age Group': '36-45', 'January': '15%', 'February': '18%', 'March': '17%', 'April': '18%', 'May': '20%'},
    {'Age Group': '46-55', 'January': '25%', 'February': '24%', 'March': '23%', 'April': '22%', 'May': '22%'}
]

# Convert percentage strings to floats
for entry in data:
    for key, value in entry.items():
        if '%' in value:
            entry[key] = float(value.strip('%')) / 100

# Extracting age groups and months data
age_groups = [entry['Age Group'] for entry in data]
months = ['January', 'February', 'March', 'April', 'May']

# Extracting data per month to stack
stack_data = {month: [entry[month] for entry in data] for month in months}

# Setting up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Bar locations
bar_locs = range(len(age_groups))

# Stacking each month's data
cumulative_values = [0] * len(age_groups)
for month in months:
    ax.bar(age_groups, stack_data[month], bottom=cumulative_values, label=month)
    # Update the bottom for the next stack
    cumulative_values = [cum_value + stack_data[month][i] for i, cum_value in enumerate(cumulative_values)]

# Formatting the plot
ax.set_title('Percentage Distribution by Age Group and Month')
ax.set_xlabel('Age Group')
ax.set_ylabel('Percentage (%)')
ax.legend(title='Months')

# Adding the values on top of the stacks
for i, age_group in enumerate(age_groups):
    for month, values in stack_data.items():
        height = sum([stack_data[m][i] for m in months[:months.index(month) + 1]])
        ax.text(i, height, f"{values[i]*100:.0f}%", ha='center')

# Show the plot
plt.show()