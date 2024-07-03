
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Your input data
data = [
    {'Age Group': '0-8', 'Reading': 15, 'Watching TV': 35, 'Playing Video Games': 40, 'Exercising': 10},
    {'Age Group': '9-18', 'Reading': 25, 'Watching TV': 30, 'Playing Video Games': 35, 'Exercising': 10},
    {'Age Group': '19-34', 'Reading': 20, 'Watching TV': 25, 'Playing Video Games': 30, 'Exercising': 25},
    {'Age Group': '35-50', 'Reading': 30, 'Watching TV': 25, 'Playing Video Games': 25, 'Exercising': 20},
    {'Age Group': '51-65', 'Reading': 20, 'Watching TV': 30, 'Playing Video Games': 20, 'Exercising': 30},
    {'Age Group': '66+', 'Reading': 25, 'Watching TV': 35, 'Playing Video Games': 10, 'Exercising': 30}
]

# Convert into pandas DataFrame
df = pd.DataFrame(data)
df.set_index('Age Group', inplace=True)

# Calculate the percentage for 100% stacked bar
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Plotting
fig, ax = plt.subplots(figsize=(12, 10))

bar_width = 0.8
categories = df_percentage.index
colors = ['#4daf4a', '#377eb8', '#ff7f00', '#984ea3']

# Initial bottom to stack the bars
bottom = [0] * len(df_percentage)

for i, col in enumerate(df.columns):
    ax.bar(categories, df_percentage[col], bar_width, label=col, color=colors[i], bottom=bottom)
    # Update the bottom to stack the next layer of bars
    bottom = bottom + df_percentage[col].values

# Beautify the plot
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Time Spent on Leisure Activities by Age Group')
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.05))

# Display the percentages on the bars
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    if height > 0:  # To avoid clutter, only display if height is significant
        ax.text(x + width / 2,
                y + height / 2,
                f"{height:.1f}%",
                ha='center',
                va='center')

# Show the plot
plt.tight_layout()
plt.show()