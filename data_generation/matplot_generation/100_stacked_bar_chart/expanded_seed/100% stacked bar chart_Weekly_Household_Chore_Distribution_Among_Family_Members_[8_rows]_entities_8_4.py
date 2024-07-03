
import matplotlib.pyplot as plt
import pandas as pd

# Provided data
data = [
    {'Member': 'Alice', 'Cleaning': 20, 'Laundry': 20, 'Grocery Shopping': 5, 'Cooking': 10, 'Yard Work': 0, 'Bills and Finances': 15, 'Pet Care': 10, 'Child Care': 20},
    {'Member': 'Bob', 'Cleaning': 15, 'Laundry': 0, 'Grocery Shopping': 20, 'Cooking': 35, 'Yard Work': 25, 'Bills and Finances': 5, 'Pet Care': 5, 'Child Care': 0},
    {'Member': 'Charlie', 'Cleaning': 10, 'Laundry': 0, 'Grocery Shopping': 0, 'Cooking': 5, 'Yard Work': 0, 'Bills and Finances': 0, 'Pet Care': 15, 'Child Care': 70},
    {'Member': 'Diana', 'Cleaning': 30, 'Laundry': 10, 'Grocery Shopping': 60, 'Cooking': 40, 'Yard Work': 20, 'Bills and Finances': 10, 'Pet Care': 0, 'Child Care': 30},
    {'Member': 'Eve', 'Cleaning': 15, 'Laundry': 60, 'Grocery Shopping': 10, 'Cooking': 5, 'Yard Work': 5, 'Bills and Finances': 70, 'Pet Care': 15, 'Child Care': 15},
    {'Member': 'Felix', 'Cleaning': 5, 'Laundry': 5, 'Grocery Shopping': 5, 'Cooking': 0, 'Yard Work': 45, 'Bills and Finances': 0, 'Pet Care': 35, 'Child Care': 5},
    {'Member': 'Grace', 'Cleaning': 5, 'Laundry': 5, 'Grocery Shopping': 0, 'Cooking': 5, 'Yard Work': 5, 'Bills and Finances': 0, 'Pet Care': 20, 'Child Care': 60},
    {'Member': 'Haley', 'Cleaning': 0, 'Laundry': 0, 'Grocery Shopping': 0, 'Cooking': 0, 'Yard Work': 0, 'Bills and Finances': 0, 'Pet Care': 0, 'Child Care': 0}
]

# Convert to DataFrame
df = pd.DataFrame(data)
members = df['Member']
tasks = df.columns[1:]
df.set_index('Member', inplace=True)

# Normalize the data to get percentages
df_normalized = df.div(df.sum(axis=1), axis=0)

# Plotting the 100% stacked bar chart
fig, ax = plt.subplots()

bar_width = 0.5
colors = plt.cm.tab20.colors  # Using the tab20 colormap for variety

# Initialize bottom position for stacking bars
bottoms = [0] * len(members)
for index, task in enumerate(tasks):
    ax.bar(members, df_normalized[task], bar_width, bottom=bottoms, color=colors[index], label=task)
    # Update bottoms for the next stack
    bottoms += df_normalized[task]

ax.set_xlabel('Household Members')
ax.set_ylabel('Percentage of Tasks')
ax.set_title('100% Stacked Bar Chart of Household Tasks Distribution')
ax.legend(title='Tasks', bbox_to_anchor=(1.05, 1), loc='upper left')  # Place the legend outside the plot

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the plot
plt.show()