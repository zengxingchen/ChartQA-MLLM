
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = [
    {'Year': 2018, 'Startups (%)': 20, 'Research (%)': 30, 'Development (%)': 25, 'Marketing (%)': 15, 'Sales (%)': 10},
    {'Year': 2019, 'Startups (%)': 25, 'Research (%)': 25, 'Development (%)': 20, 'Marketing (%)': 20, 'Sales (%)': 10},
    {'Year': 2020, 'Startups (%)': 30, 'Research (%)': 20, 'Development (%)': 30, 'Marketing (%)': 10, 'Sales (%)': 10},
    {'Year': 2021, 'Startups (%)': 35, 'Research (%)': 15, 'Development (%)': 25, 'Marketing (%)': 15, 'Sales (%)': 10},
    {'Year': 2022, 'Startups (%)': 40, 'Research (%)': 10, 'Development (%)': 20, 'Marketing (%)': 20, 'Sales (%)': 10},
    {'Year': 2023, 'Startups (%)': 45, 'Research (%)': 5, 'Development (%)': 15, 'Marketing (%)': 25, 'Sales (%)': 10}
]

# Convert the dictionary list to a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Year'
df.set_index('Year', inplace=True)

# Calculate the cumulative sum of the percentages to stack them correctly
cumulative_values = df.cumsum(axis=1)

# Create the 100% stacked bar chart using matplotlib
colors = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e']  # Custom color codes
fig, ax = plt.subplots(figsize=(10, 14))  # Change the width and height of the chart

bar_width = 0.6  # Adjust the bar width
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
ax.set_title('Investment Distribution in Business Areas Over Years', pad=20)
ax.legend(title='Business Area', bbox_to_anchor=(1.05, 1), loc='upper left')

# Change the x-ticks to percentage
xticks = ax.get_xticks()
ax.set_xticklabels(['{}%'.format(int(x)) for x in xticks])

plt.tight_layout()

# Display the plot
plt.show()