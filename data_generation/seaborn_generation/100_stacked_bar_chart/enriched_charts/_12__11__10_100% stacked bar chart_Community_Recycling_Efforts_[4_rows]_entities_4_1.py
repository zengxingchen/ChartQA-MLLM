
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = [
    {'Year': 2018, 'Exercise (%)': 15, 'Diet (%)': 20, 'Mental Health (%)': 25, 'Sleep (%)': 30, 'Socializing (%)': 10},
    {'Year': 2019, 'Exercise (%)': 20, 'Diet (%)': 25, 'Mental Health (%)': 20, 'Sleep (%)': 25, 'Socializing (%)': 10},
    {'Year': 2020, 'Exercise (%)': 25, 'Diet (%)': 30, 'Mental Health (%)': 15, 'Sleep (%)': 20, 'Socializing (%)': 10},
    {'Year': 2021, 'Exercise (%)': 30, 'Diet (%)': 35, 'Mental Health (%)': 10, 'Sleep (%)': 15, 'Socializing (%)': 10},
    {'Year': 2022, 'Exercise (%)': 35, 'Diet (%)': 30, 'Mental Health (%)': 10, 'Sleep (%)': 15, 'Socializing (%)': 10},
    {'Year': 2023, 'Exercise (%)': 40, 'Diet (%)': 25, 'Mental Health (%)': 10, 'Sleep (%)': 15, 'Socializing (%)': 10}
]

# Convert the dictionary list to a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Year'
df.set_index('Year', inplace=True)

# Calculate the cumulative sum of the percentages to stack them correctly
cumulative_values = df.cumsum(axis=1)

# Create the 100% stacked bar chart using matplotlib
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2']  # Custom color codes
fig, ax = plt.subplots(figsize=(12, 8))  # Change the width and height of the chart

bar_width = 0.6  # Adjust the bar width
for i, col in enumerate(df.columns):
    # We'll plot the bottom values for all but the first column (i.e., index 0)
    bottom_values = cumulative_values.iloc[:, i-1] if i > 0 else None
    ax.bar(
        df.index,
        df[col],
        bottom=bottom_values,
        color=colors[i],
        edgecolor='white',
        label=col,
        width=bar_width
    )

# Add some customizations
ax.set_xticks(df.index)
ax.set_xticklabels(df.index)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Health Activity Distribution Over Years', pad=20)
ax.legend(title='Health Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Change the y-ticks to percentage
yticks = ax.get_yticks()
ax.set_yticklabels(['{}%'.format(int(y)) for y in yticks])

plt.tight_layout()

# Display the plot
plt.show()