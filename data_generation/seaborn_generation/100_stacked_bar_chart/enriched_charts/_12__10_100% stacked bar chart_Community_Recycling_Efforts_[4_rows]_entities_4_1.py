
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = [
    {'Year': 2018, 'Movies (%)': 20, 'Music (%)': 25, 'Sports (%)': 30, 'Travel (%)': 15, 'Reading (%)': 10},
    {'Year': 2019, 'Movies (%)': 22, 'Music (%)': 24, 'Sports (%)': 28, 'Travel (%)': 16, 'Reading (%)': 10},
    {'Year': 2020, 'Movies (%)': 24, 'Music (%)': 23, 'Sports (%)': 26, 'Travel (%)': 17, 'Reading (%)': 10},
    {'Year': 2021, 'Movies (%)': 26, 'Music (%)': 22, 'Sports (%)': 24, 'Travel (%)': 18, 'Reading (%)': 10},
    {'Year': 2022, 'Movies (%)': 28, 'Music (%)': 21, 'Sports (%)': 22, 'Travel (%)': 19, 'Reading (%)': 10}
]

# Convert the dictionary list to a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Year'
df.set_index('Year', inplace=True)

# Calculate the cumulative sum of the percentages to stack them correctly
cumulative_values = df.cumsum(axis=1)

# Create the 100% stacked bar chart using matplotlib
colors = ['#2E86C1', '#AF7AC5', '#F39C12', '#E74C3C', '#58D68D']  # Custom color codes
fig, ax = plt.subplots(figsize=(10, 7))  # Change the width and height of the chart

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
ax.set_title('Distribution of Interests in Leisure Activities Over Years', pad=20)
ax.legend(title='Leisure Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Change the y-ticks to percentage
yticks = ax.get_yticks()
ax.set_yticklabels(['{}%'.format(int(y)) for y in yticks])

plt.tight_layout()

# Display the plot
plt.show()