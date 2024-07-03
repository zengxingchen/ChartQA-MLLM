
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Your input data
data = [
    {'Age Group': '0-8', 'TV': 30, 'Computer': 10, 'Mobile Device': 40, 'Video Game Console': 20},
    {'Age Group': '9-18', 'TV': 15, 'Computer': 30, 'Mobile Device': 40, 'Video Game Console': 15},
    {'Age Group': '19-34', 'TV': 10, 'Computer': 25, 'Mobile Device': 50, 'Video Game Console': 15},
    {'Age Group': '35-50', 'TV': 25, 'Computer': 35, 'Mobile Device': 30, 'Video Game Console': 10}
]

# Convert into pandas DataFrame
df = pd.DataFrame(data)
df.set_index('Age Group', inplace=True)

# Calculate the percentage for 100% stacked bar
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.85
categories = df_percentage.index
colors = sns.color_palette("Set3", 4)

# Initial bottom to stack the bars
bottom = [0] * len(df_percentage)

for i, col in enumerate(df.columns):
    ax.bar(categories, df_percentage[col], bar_width, label=col, color=colors[i], bottom=bottom)
    # Update the bottom to stack the next layer of bars
    bottom = bottom + df_percentage[col].values

# Beautify the plot
ax.set_ylabel('Percentage')
ax.set_title('Percentage Use of Devices by Age Group')
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05))

# Display the percentages on the bars
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    if height > 0: # To avoid clutter, only display if height is significant
        ax.text(x + width/2, 
                y + height/2, 
                f"{height:.1f}%", 
                ha='center', 
                va='center')

# Show the plot
plt.tight_layout()
plt.show()