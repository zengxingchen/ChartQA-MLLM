
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = [
    {'Day': 'Monday', 'Healthy Eating': 0.15, 'Exercise': 0.20, 'Socializing': 0.10, 'Relaxation': 0.15, 'Work': 0.25, 'Leisure': 0.15},
    {'Day': 'Tuesday', 'Healthy Eating': 0.20, 'Exercise': 0.18, 'Socializing': 0.12, 'Relaxation': 0.18, 'Work': 0.22, 'Leisure': 0.10},
    {'Day': 'Wednesday', 'Healthy Eating': 0.18, 'Exercise': 0.22, 'Socializing': 0.15, 'Relaxation': 0.12, 'Work': 0.20, 'Leisure': 0.13},
    {'Day': 'Thursday', 'Healthy Eating': 0.12, 'Exercise': 0.20, 'Socializing': 0.18, 'Relaxation': 0.15, 'Work': 0.18, 'Leisure': 0.17},
    {'Day': 'Friday', 'Healthy Eating': 0.22, 'Exercise': 0.15, 'Socializing': 0.15, 'Relaxation': 0.20, 'Work': 0.15, 'Leisure': 0.13},
    {'Day': 'Saturday', 'Healthy Eating': 0.25, 'Exercise': 0.10, 'Socializing': 0.20, 'Relaxation': 0.18, 'Work': 0.12, 'Leisure': 0.15},
    {'Day': 'Sunday', 'Healthy Eating': 0.20, 'Exercise': 0.18, 'Socializing': 0.18, 'Relaxation': 0.15, 'Work': 0.15, 'Leisure': 0.14}
]

# Transform data into a pandas DataFrame
df = pd.DataFrame(data)

# Prepare data for 100% stacked bar chart
df.set_index('Day', inplace=True)
df.sort_index(inplace=True)

# Calculate cumulative sum for stacking
cumsum_df = df.cumsum(axis=1)

# Start plotting
fig, ax = plt.subplots(figsize=(12, 8))  # Changed figure size for better clarity

# Plotting each layer of the stacked bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF6', '#FF8C33']
width = 0.7  # Adjusted width of the bars
for i, col in enumerate(df.columns):
    ax.bar(df.index, df[col], bottom=cumsum_df[col] - df[col], color=colors[i], edgecolor='white', width=width)

# Customizing the plot
plt.xticks(rotation=0)
plt.yticks(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['0%', '20%', '40%', '60%', '80%', '100%'])
plt.xlabel('Day of the Week')
plt.ylabel('Percentage')
plt.title('Daily Activities Distribution', pad=20)
plt.legend(df.columns, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the plot
plt.show()