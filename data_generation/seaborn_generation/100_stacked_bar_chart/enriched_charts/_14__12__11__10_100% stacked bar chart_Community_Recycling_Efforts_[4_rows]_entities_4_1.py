
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = [
    {'Year': 2018, 'Carbon Emissions (tons)': 25, 'Renewable Energy (%)': 10, 'Recycling Rate (%)': 15, 'Air Quality Index': 45, 'Green Spaces (%)': 20},
    {'Year': 2019, 'Carbon Emissions (tons)': 20, 'Renewable Energy (%)': 15, 'Recycling Rate (%)': 20, 'Air Quality Index': 40, 'Green Spaces (%)': 25},
    {'Year': 2020, 'Carbon Emissions (tons)': 15, 'Renewable Energy (%)': 20, 'Recycling Rate (%)': 25, 'Air Quality Index': 35, 'Green Spaces (%)': 30},
    {'Year': 2021, 'Carbon Emissions (tons)': 10, 'Renewable Energy (%)': 25, 'Recycling Rate (%)': 30, 'Air Quality Index': 30, 'Green Spaces (%)': 35},
    {'Year': 2022, 'Carbon Emissions (tons)': 10, 'Renewable Energy (%)': 30, 'Recycling Rate (%)': 35, 'Air Quality Index': 25, 'Green Spaces (%)': 30},
    {'Year': 2023, 'Carbon Emissions (tons)': 5, 'Renewable Energy (%)': 35, 'Recycling Rate (%)': 40, 'Air Quality Index': 20, 'Green Spaces (%)': 25}
]

# Convert the dictionary list to a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Year'
df.set_index('Year', inplace=True)

# Calculate the cumulative sum of the percentages to stack them correctly
cumulative_values = df.cumsum(axis=1)

# Create the 100% stacked bar chart using matplotlib
colors = ['#4CAF50', '#2196F3', '#FFC107', '#FF5722', '#9C27B0']  # Custom color codes
fig, ax = plt.subplots(figsize=(10, 12))  # Change the width and height of the chart

bar_width = 0.5  # Adjust the bar width
for i, col in enumerate(df.columns):
    # We'll plot the bottom values for all but the first column (i.e., index 0)
    bottom_values = cumulative_values.iloc[:, i-1] if i > 0 else None
    ax.barh(
        df.index,
        df[col],
        left=bottom_values,
        color=colors[i],
        edgecolor='white',
        label=col,
        height=bar_width
    )

# Add some customizations
ax.set_yticks(df.index)
ax.set_yticklabels(df.index)
ax.set_ylabel('Year')
ax.set_xlabel('Percentage')
ax.set_title('Environmental Metrics Over Years', pad=20)
ax.legend(title='Environmental Metric', bbox_to_anchor=(1.05, 1), loc='upper left')

# Change the x-ticks to percentage
xticks = ax.get_xticks()
ax.set_xticklabels(['{}%'.format(int(x)) for x in xticks])

plt.tight_layout()

# Display the plot
plt.show()