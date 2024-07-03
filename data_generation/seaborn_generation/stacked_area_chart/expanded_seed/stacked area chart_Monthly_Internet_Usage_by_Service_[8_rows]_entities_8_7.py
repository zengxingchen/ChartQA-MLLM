
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Our provided data in list of dictionaries format
data = [
    {'Month': '2023-01', 'Streaming': 150, 'Online Gaming': 100, 'Social Media': 200, 'Remote Work': 250, 'Education': 50},
    {'Month': '2023-02', 'Streaming': 160, 'Online Gaming': 110, 'Social Media': 210, 'Remote Work': 260, 'Education': 60},
    {'Month': '2023-03', 'Streaming': 170, 'Online Gaming': 90, 'Social Media': 205, 'Remote Work': 270, 'Education': 65},
    {'Month': '2023-04', 'Streaming': 180, 'Online Gaming': 95, 'Social Media': 215, 'Remote Work': 280, 'Education': 70},
    {'Month': '2023-05', 'Streaming': 190, 'Online Gaming': 85, 'Social Media': 220, 'Remote Work': 290, 'Education': 75},
    {'Month': '2023-06', 'Streaming': 200, 'Online Gaming': 80, 'Social Media': 230, 'Remote Work': 300, 'Education': 80},
    {'Month': '2023-07', 'Streaming': 210, 'Online Gaming': 75, 'Social Media': 235, 'Remote Work': 310, 'Education': 85},
    {'Month': '2023-08', 'Streaming': 220, 'Online Gaming': 70, 'Social Media': 240, 'Remote Work': 320, 'Education': 90}
]

# Converting our data to a DataFrame
df = pd.DataFrame(data)

# Reshaping the dataframe to a long format
df_long = df.melt(id_vars='Month', var_name='Category', value_name='Usage')

# Convert 'Month' to a datetime to sort by date correctly
df_long['Month'] = pd.to_datetime(df_long['Month'])

# Sorting the values is important to plot correctly
df_long.sort_values(by=['Month', 'Category'], inplace=True)

# Setting the color palette to be used for the lines
palette = sns.color_palette('husl', len(df_long['Category'].unique()))

# Start plotting
plt.figure(figsize=(10, 7))
ax = plt.subplot(111)

# Grouping data by category to plot each layer
for i, category in enumerate(df_long['Category'].unique()[::-1]):
    df_subset = df_long[df_long['Category'] == category]
    # Lineplot for each category
    sns.lineplot(data=df_subset, x='Month', y='Usage', color=palette[i], label=category)
    if i == 0:
        ax.fill_between(df_subset['Month'], 0, df_subset['Usage'], color=palette[i], alpha=0.5)
    else:
        sum_usage = df_long[df_long['Category'].isin(df_long['Category'].unique()[:i])].groupby('Month').sum()['Usage']
        ax.fill_between(df_subset['Month'], sum_usage, sum_usage + df_subset['Usage'], color=palette[i], alpha=0.5)

# Formatting the x-axis labels to display the month properly
ax.xaxis.set_major_locator(MaxNLocator(nbins=len(df) + 1))
ax.set_xticklabels([d.strftime('%Y-%m') for d in df['Month']], rotation=45, ha='right')

# Additional formatting
plt.title('Usage Trends by Category Over Months')
plt.ylabel('Usage')
plt.xlabel('Month')
plt.legend(loc='upper left')

# Display the plot
plt.tight_layout()
plt.show()