
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Data
data = {
    'Job Role': ['Student', 'Teacher', 'Office Worker', 'Retiree', 'Freelancer'],
    'Reading': [15, 10, 5, 20, 10],
    'Exercise': [10, 5, 15, 10, 10],
    'Meditation': [5, 10, 10, 15, 20],
    'Work': [40, 50, 60, 10, 30],
    'Leisure': [20, 15, 5, 30, 20],
    'Socializing': [10, 10, 5, 15, 10]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Calculate the percentage
df.set_index('Job Role', inplace=True)
df_percentage = df.divide(df.sum(axis=1), axis=0) * 100

# Start a figure with seaborn style
plt.figure(figsize=(10, 12))
sns.set_theme(style="whitegrid")

# Create a color map
colors = ["#3498db", "#e74c3c", "#2ecc71", "#f1c40f", "#9b59b6", "#34495e"]

# Starting position
bar_start = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0], index=df.index)

for col, color in zip(df.columns, colors):
    # Plot each category stack
    sns.barplot(
        y=df_percentage[col],
        x=df_percentage.index,
        color=color,
        label=col,
        bottom=bar_start
    )
    # Add the values to the starting position
    bar_start += df_percentage[col]

# Customizations
plt.ylabel('Percentage')
plt.xlabel('Job Role')
plt.title('Daily Activity Distribution by Job Role')
plt.xticks(rotation=45)
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Convert y-axis labels to percentage
plt.gca().yaxis.set_major_formatter(PercentFormatter())

# Show the plot
plt.tight_layout()
plt.show()