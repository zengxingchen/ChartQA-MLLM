
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Age Group": ["16-24", "25-34", "35-44", "45-54", "55-64", "65+"],
    "Cardio": [1.8, 2.0, 1.6, 1.4, 1.2, 1.0],
    "Strength": [0.5, 0.7, 0.9, 1.1, 1.3, 1.5],
    "Flexibility": [0.6, 0.8, 0.7, 0.9, 0.6, 0.5],
    "Balance": [0.3, 0.4, 0.5, 0.7, 0.6, 0.8]
}

df = pd.DataFrame(data)

# Plotting
fig, ax = plt.subplots(figsize=(10, 14))

bar_height = 0.15  # height of the bars

# Position of bars on x-axis
indices = df.index
r1 = range(len(indices))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]
r4 = [x + bar_height for x in r3]

# Make the plot
ax.bar(r1, df['Cardio'], color='#FF5733', edgecolor='white', width=bar_height, label='Cardio')
ax.bar(r2, df['Strength'], color='#33FF57', edgecolor='white', width=bar_height, label='Strength')
ax.bar(r3, df['Flexibility'], color='#3357FF', edgecolor='white', width=bar_height, label='Flexibility')
ax.bar(r4, df['Balance'], color='#FF33A1', edgecolor='white', width=bar_height, label='Balance')

# Add labels
ax.set_ylabel('Average Weekly Hours', fontsize=15)
ax.set_xlabel('Age Group', fontsize=15)
ax.set_title('Average Weekly Exercise Hours by Age Group', fontsize=18)

# Add yticks on the middle of the group bars
ax.set_xticks([r + bar_height for r in range(len(r1))])
ax.set_xticklabels(df['Age Group'])

# Set y-axis limit
ax.set_ylim(0.4, 2.2)

# Create legend & Show graphic
ax.legend(loc='upper right')
plt.tight_layout()
plt.show()