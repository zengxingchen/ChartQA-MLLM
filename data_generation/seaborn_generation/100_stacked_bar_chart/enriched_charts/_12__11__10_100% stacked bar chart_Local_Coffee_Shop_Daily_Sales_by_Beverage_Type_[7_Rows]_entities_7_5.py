
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = [
    {'Day': 'Monday', 'Impressionism': 0.20, 'Surrealism': 0.15, 'Abstract': 0.20, 'Realism': 0.15, 'Cubism': 0.10, 'Pop Art': 0.20},
    {'Day': 'Tuesday', 'Impressionism': 0.25, 'Surrealism': 0.10, 'Abstract': 0.18, 'Realism': 0.15, 'Cubism': 0.12, 'Pop Art': 0.20},
    {'Day': 'Wednesday', 'Impressionism': 0.18, 'Surrealism': 0.20, 'Abstract': 0.15, 'Realism': 0.18, 'Cubism': 0.12, 'Pop Art': 0.17},
    {'Day': 'Thursday', 'Impressionism': 0.22, 'Surrealism': 0.15, 'Abstract': 0.20, 'Realism': 0.12, 'Cubism': 0.18, 'Pop Art': 0.13},
    {'Day': 'Friday', 'Impressionism': 0.20, 'Surrealism': 0.18, 'Abstract': 0.15, 'Realism': 0.20, 'Cubism': 0.12, 'Pop Art': 0.15},
    {'Day': 'Saturday', 'Impressionism': 0.25, 'Surrealism': 0.12, 'Abstract': 0.22, 'Realism': 0.10, 'Cubism': 0.15, 'Pop Art': 0.16},
    {'Day': 'Sunday', 'Impressionism': 0.22, 'Surrealism': 0.15, 'Abstract': 0.18, 'Realism': 0.18, 'Cubism': 0.12, 'Pop Art': 0.15}
]

# Transform data into a pandas DataFrame
df = pd.DataFrame(data)

# Prepare data for 100% stacked bar chart
df.set_index('Day', inplace=True)
df.sort_index(inplace=True)

# Calculate cumulative sum for stacking
cumsum_df = df.cumsum(axis=1)

# Start plotting
fig, ax = plt.subplots(figsize=(8, 12))

# Plotting each layer of the stacked bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF6', '#FF8C33']
width = 0.7  # Change the width of the bars
for i, col in enumerate(df.columns):
    ax.bar(df.index, df[col], bottom=cumsum_df[col] - df[col], color=colors[i], edgecolor='white', width=width)

# Customizing the plot
plt.xticks(rotation=0)
plt.yticks(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['0%', '20%', '40%', '60%', '80%', '100%'])
plt.xlabel('Day of the Week')
plt.ylabel('Percentage')
plt.title('Art Movement Preferences by Day', pad=20)
plt.legend(df.columns, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the plot
plt.show()