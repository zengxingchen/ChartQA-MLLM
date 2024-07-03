
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = [
    {'Day': 'Monday', 'Pop': '25%', 'Rock': '20%', 'Jazz': '20%', 'Classical': '15%', 'Hip-Hop': '10%', 'Electronic': '10%'},
    {'Day': 'Tuesday', 'Pop': '22%', 'Rock': '24%', 'Jazz': '18%', 'Classical': '16%', 'Hip-Hop': '10%', 'Electronic': '10%'},
    {'Day': 'Wednesday', 'Pop': '20%', 'Rock': '26%', 'Jazz': '19%', 'Classical': '15%', 'Hip-Hop': '10%', 'Electronic': '10%'},
    {'Day': 'Thursday', 'Pop': '18%', 'Rock': '25%', 'Jazz': '20%', 'Classical': '17%', 'Hip-Hop': '10%', 'Electronic': '10%'},
    {'Day': 'Friday', 'Pop': '30%', 'Rock': '20%', 'Jazz': '15%', 'Classical': '15%', 'Hip-Hop': '10%', 'Electronic': '10%'},
    {'Day': 'Saturday', 'Pop': '35%', 'Rock': '15%', 'Jazz': '15%', 'Classical': '15%', 'Hip-Hop': '10%', 'Electronic': '10%'},
    {'Day': 'Sunday', 'Pop': '28%', 'Rock': '18%', 'Jazz': '17%', 'Classical': '17%', 'Hip-Hop': '10%', 'Electronic': '10%'}
]

# Transform data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert percentage strings to numerical values
for col in df.columns:
    if col != 'Day':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

# Prepare data for 100% stacked bar chart
df.set_index('Day', inplace=True)
df.sort_index(inplace=True)

# Calculate cumulative sum for stacking
cumsum_df = df.cumsum(axis=1)

# Start plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting each layer of the stacked bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FFD133', '#33FFD1']
width = 0.8  # Change the width of the bars
for i, col in enumerate(df.columns):
    ax.bar(df.index, df[col], bottom=cumsum_df[col] - df[col], color=colors[i], edgecolor='white', width=width)

# Customizing the plot
plt.xticks(rotation=0)
plt.yticks(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['0%', '20%', '40%', '60%', '80%', '100%'])
plt.xlabel('Day of the Week')
plt.ylabel('Percentage')
plt.title('Daily Music Genre Preferences', pad=20)
plt.legend(df.columns, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the plot
plt.show()