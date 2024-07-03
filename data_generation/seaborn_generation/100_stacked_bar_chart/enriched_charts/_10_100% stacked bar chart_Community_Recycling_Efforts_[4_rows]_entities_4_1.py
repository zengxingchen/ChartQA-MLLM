
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = [
    {'Year': 2018, 'Science (%)': 25, 'Technology (%)': 30, 'Engineering (%)': 20, 'Mathematics (%)': 15, 'Arts (%)': 10},
    {'Year': 2019, 'Science (%)': 30, 'Technology (%)': 25, 'Engineering (%)': 25, 'Mathematics (%)': 10, 'Arts (%)': 10},
    {'Year': 2020, 'Science (%)': 35, 'Technology (%)': 20, 'Engineering (%)': 30, 'Mathematics (%)': 5, 'Arts (%)': 10},
    {'Year': 2021, 'Science (%)': 40, 'Technology (%)': 15, 'Engineering (%)': 25, 'Mathematics (%)': 10, 'Arts (%)': 10},
    {'Year': 2022, 'Science (%)': 45, 'Technology (%)': 10, 'Engineering (%)': 20, 'Mathematics (%)': 15, 'Arts (%)': 10}
]

# Convert the dictionary list to a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Year'
df.set_index('Year', inplace=True)

# Calculate the cumulative sum of the percentages to stack them correctly
cumulative_values = df.cumsum(axis=1)

# Create the 100% stacked bar chart using matplotlib
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']  # Custom color codes
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
ax.set_xticklabels(df.index, rotation=0)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Distribution of Interests in STEM and Arts Over Years', pad=20)
ax.legend(title='Field of Study', bbox_to_anchor=(1.05, 1), loc='upper left')

# Change the y-ticks to percentage
yticks = ax.get_yticks()
ax.set_yticklabels(['{}%'.format(int(y)) for y in yticks])

plt.tight_layout()

# Display the plot
plt.show()