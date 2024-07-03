
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = [
    {'Day': 'Monday', 'Democracy': 0.25, 'Economy': 0.20, 'Healthcare': 0.15, 'Education': 0.10, 'Environment': 0.20, 'Security': 0.10},
    {'Day': 'Tuesday', 'Democracy': 0.20, 'Economy': 0.25, 'Healthcare': 0.10, 'Education': 0.15, 'Environment': 0.20, 'Security': 0.10},
    {'Day': 'Wednesday', 'Democracy': 0.18, 'Economy': 0.22, 'Healthcare': 0.15, 'Education': 0.12, 'Environment': 0.20, 'Security': 0.13},
    {'Day': 'Thursday', 'Democracy': 0.22, 'Economy': 0.18, 'Healthcare': 0.20, 'Education': 0.10, 'Environment': 0.15, 'Security': 0.15},
    {'Day': 'Friday', 'Democracy': 0.20, 'Economy': 0.20, 'Healthcare': 0.15, 'Education': 0.18, 'Environment': 0.12, 'Security': 0.15},
    {'Day': 'Saturday', 'Democracy': 0.25, 'Economy': 0.18, 'Healthcare': 0.20, 'Education': 0.12, 'Environment': 0.10, 'Security': 0.15},
    {'Day': 'Sunday', 'Democracy': 0.20, 'Economy': 0.15, 'Healthcare': 0.22, 'Education': 0.13, 'Environment': 0.18, 'Security': 0.12}
]

# Transform data into a pandas DataFrame
df = pd.DataFrame(data)

# Prepare data for 100% stacked bar chart
df.set_index('Day', inplace=True)
df.sort_index(inplace=True)

# Calculate cumulative sum for stacking
cumsum_df = df.cumsum(axis=1)

# Start plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting each layer of the stacked bar
colors = ['#E74C3C', '#3498DB', '#2ECC71', '#F1C40F', '#9B59B6', '#E67E22']
width = 0.6  # Change the width of the bars
for i, col in enumerate(df.columns):
    ax.bar(df.index, df[col], bottom=cumsum_df[col] - df[col], color=colors[i], edgecolor='white', width=width)

# Customizing the plot
plt.xticks(rotation=0)
plt.yticks(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['0%', '20%', '40%', '60%', '80%', '100%'])
plt.xlabel('Day of the Week')
plt.ylabel('Percentage')
plt.title('Public Interest in Governance Issues by Day', pad=20)
plt.legend(df.columns, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the plot
plt.show()