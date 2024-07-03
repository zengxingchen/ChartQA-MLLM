
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Age Group": ["16-24", "25-34", "35-44", "45-54", "55-64", "65+"],
    "Reading": [1.8, 2.0, 2.3, 2.5, 2.8, 3.0],
    "Watching TV": [3.0, 2.8, 2.5, 2.2, 2.0, 1.8],
    "Playing Sports": [1.5, 1.8, 1.7, 1.4, 1.2, 0.9],
    "Video Games": [2.5, 2.1, 1.9, 1.5, 1.0, 0.8],
    "Cooking": [1.2, 1.5, 1.8, 2.0, 2.3, 2.5]
}

df = pd.DataFrame(data)

# Plotting
fig, ax = plt.subplots(figsize=(10, 14))

bar_width = 0.2  # width of the bars

# Position of bars on x-axis
indices = df.index
r1 = range(len(indices))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
r5 = [x + bar_width for x in r4]

# Make the plot
ax.bar(r1, df['Reading'], color='#FF5733', edgecolor='white', width=bar_width, label='Reading')
ax.bar(r2, df['Watching TV'], color='#33FF57', edgecolor='white', width=bar_width, label='Watching TV')
ax.bar(r3, df['Playing Sports'], color='#3357FF', edgecolor='white', width=bar_width, label='Playing Sports')
ax.bar(r4, df['Video Games'], color='#FF33A1', edgecolor='white', width=bar_width, label='Video Games')
ax.bar(r5, df['Cooking'], color='#FFBD33', edgecolor='white', width=bar_width, label='Cooking')

# Add labels
ax.set_ylabel('Average Daily Hours', fontsize=15)
ax.set_xlabel('Age Group', fontsize=15)
ax.set_title('Average Daily Hours Spent on Various Hobbies by Age Group', fontsize=18, y=1.02)

# Add xticks on the middle of the group bars
ax.set_xticks([r + 2 * bar_width for r in range(len(r1))])
ax.set_xticklabels(df['Age Group'])

# Set y-axis limits
ax.set_ylim(0.5, 3.5)

# Create legend & Show graphic
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()