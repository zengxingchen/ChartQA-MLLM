
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = [
    {'Day': 'Monday', 'Cardio': 0.25, 'Strength Training': 0.20, 'Flexibility': 0.15, 'Yoga': 0.15, 'Pilates': 0.10, 'Aerobics': 0.15},
    {'Day': 'Tuesday', 'Cardio': 0.20, 'Strength Training': 0.22, 'Flexibility': 0.18, 'Yoga': 0.15, 'Pilates': 0.10, 'Aerobics': 0.15},
    {'Day': 'Wednesday', 'Cardio': 0.18, 'Strength Training': 0.25, 'Flexibility': 0.17, 'Yoga': 0.20, 'Pilates': 0.10, 'Aerobics': 0.10},
    {'Day': 'Thursday', 'Cardio': 0.20, 'Strength Training': 0.18, 'Flexibility': 0.15, 'Yoga': 0.25, 'Pilates': 0.12, 'Aerobics': 0.10},
    {'Day': 'Friday', 'Cardio': 0.22, 'Strength Training': 0.20, 'Flexibility': 0.15, 'Yoga': 0.18, 'Pilates': 0.10, 'Aerobics': 0.15},
    {'Day': 'Saturday', 'Cardio': 0.30, 'Strength Training': 0.15, 'Flexibility': 0.12, 'Yoga': 0.20, 'Pilates': 0.10, 'Aerobics': 0.13},
    {'Day': 'Sunday', 'Cardio': 0.28, 'Strength Training': 0.18, 'Flexibility': 0.15, 'Yoga': 0.15, 'Pilates': 0.12, 'Aerobics': 0.12}
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
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF6', '#FF8C33']
width = 0.5  # Change the width of the bars
for i, col in enumerate(df.columns):
    ax.bar(df.index, df[col], bottom=cumsum_df[col] - df[col], color=colors[i], edgecolor='white', width=width)

# Customizing the plot
plt.xticks(rotation=45)
plt.yticks(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['0%', '20%', '40%', '60%', '80%', '100%'])
plt.xlabel('Day of the Week')
plt.ylabel('Percentage')
plt.title('Percentage of Different Exercises Done by Day', pad=20)
plt.legend(df.columns, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the plot
plt.show()