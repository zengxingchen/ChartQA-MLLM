
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given table data
data = [
    {'Date': '2023-03-01', '0-12 years': 25, '13-18 years': 15, '19-35 years': 30, '36-60 years': 27, '60+ years': 10},
    {'Date': '2023-03-02', '0-12 years': 30, '13-18 years': 18, '19-35 years': 45, '36-60 years': 23, '60+ years': 12},
    # ... include all data entries (omitted for brevity)
    {'Date': '2023-03-12', '0-12 years': 50, '13-18 years': 18, '19-35 years': 90, '36-60 years': 38, '60+ years': 19}
]

# Convert the chart data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Melting the dataframe to have 'Age Group' and 'Count' columns
df_long = df.melt(id_vars='Date', var_name='Age Group', value_name='Count')

# Plot a scatterplot
plt.figure(figsize=(14, 8))

# Diversify the markers and colors
markers = ['o', 's', 'X', '^', 'P']  # Different markers for each age group
palette = sns.color_palette("tab10")  # Let's use a palette of 10 colors

# Create a scatterplot using seaborn
scatterplot = sns.scatterplot(
    data=df_long,
    x='Date',
    y='Count',
    hue='Age Group',
    style='Age Group',
    palette=palette,
    markers=markers,
    s=100  # Size of the markers
)

scatterplot.set_title('Age Group Count Over Time')
scatterplot.set_xlabel('Date')
scatterplot.set_ylabel('Count')

# Rotate date labels for better visibility
plt.xticks(rotation=45)

# Show the legend
plt.legend(title='Age Group', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()