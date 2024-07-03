
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = [
    {'Year': 2018, 'Fruits (%)': 20, 'Vegetables (%)': 25, 'Grains (%)': 30, 'Proteins (%)': 15, 'Dairy (%)': 10},
    {'Year': 2019, 'Fruits (%)': 25, 'Vegetables (%)': 20, 'Grains (%)': 25, 'Proteins (%)': 20, 'Dairy (%)': 10},
    {'Year': 2020, 'Fruits (%)': 30, 'Vegetables (%)': 20, 'Grains (%)': 20, 'Proteins (%)': 20, 'Dairy (%)': 10},
    {'Year': 2021, 'Fruits (%)': 35, 'Vegetables (%)': 15, 'Grains (%)': 25, 'Proteins (%)': 15, 'Dairy (%)': 10},
    {'Year': 2022, 'Fruits (%)': 40, 'Vegetables (%)': 10, 'Grains (%)': 20, 'Proteins (%)': 20, 'Dairy (%)': 10}
]

# Convert the dictionary list to a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Year'
df.set_index('Year', inplace=True)

# Calculate the cumulative sum of the percentages to stack them correctly
cumulative_values = df.cumsum(axis=1)

# Create the 100% stacked bar chart using matplotlib
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD']  # Custom color codes
fig, ax = plt.subplots(figsize=(10, 6))  # Change the width and height of the chart

bar_width = 0.5  # Adjust the bar width
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
ax.set_xticklabels(df.index, rotation=0)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Distribution of Food Categories Over Years', pad=20)
ax.legend(title='Food Category', bbox_to_anchor=(1.05, 1), loc='upper left')

# Change the y-ticks to percentage
yticks = ax.get_yticks()
ax.set_yticklabels(['{}%'.format(int(y)) for y in yticks])

plt.tight_layout()

# Display the plot
plt.show()