
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = [
    {'Year': 2018, 'Paper (%)': 30, 'Plastic (%)': 25, 'Glass (%)': 15, 'Metals (%)': 10, 'Organics (%)': 20},
    {'Year': 2019, 'Paper (%)': 35, 'Plastic (%)': 20, 'Glass (%)': 20, 'Metals (%)': 10, 'Organics (%)': 15},
    {'Year': 2020, 'Paper (%)': 40, 'Plastic (%)': 15, 'Glass (%)': 20, 'Metals (%)': 15, 'Organics (%)': 10},
    {'Year': 2021, 'Paper (%)': 45, 'Plastic (%)': 10, 'Glass (%)': 25, 'Metals (%)': 10, 'Organics (%)': 10}
]

# Convert the dictionary list to a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Year'
df.set_index('Year', inplace=True)

# Calculate the cumulative sum of the percentages to stack them correctly
cumulative_values = df.cumsum(axis=1)

# Create the 100% stacked bar chart using matplotlib
colors = plt.get_cmap('tab20').colors  # Using the tab20 colormap for unique colors
fig, ax = plt.subplots()

for i, col in enumerate(df.columns):
    # We'll plot the bottom values for all but the first column (i.e., index 0)
    bottom_values = cumulative_values.iloc[:, i-1] if i > 0 else None
    ax.bar(
        df.index,
        df[col],
        bottom=bottom_values,
        color=colors[i],
        edgecolor='white',
        label=col
    )

# Add some customizations
ax.set_xticks(df.index)
ax.set_xticklabels(df.index, rotation=0)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('100% Stacked Bar Chart')
ax.legend(title='Material Type', bbox_to_anchor=(1.05, 1), loc='upper left')

# Change the y-ticks to percentage
yticks = ax.get_yticks()
ax.set_yticklabels(['{}%'.format(int(y)) for y in yticks])

plt.tight_layout()

# Display the plot
plt.show()