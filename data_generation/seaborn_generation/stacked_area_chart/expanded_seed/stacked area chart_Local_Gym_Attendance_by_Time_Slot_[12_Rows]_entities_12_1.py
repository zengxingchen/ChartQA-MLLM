
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your chart table data
data = [
    {'Date': '2023-03-01', 'Early Morning (5-8 AM)': 30, 'Late Morning (9 AM-12 PM)': 45, 'Afternoon (1-4 PM)': 50, 'Evening (5-9 PM)': 150, 'Night (10 PM-12 AM)': 20},
    {'Date': '2023-03-02', 'Early Morning (5-8 AM)': 28, 'Late Morning (9 AM-12 PM)': 50, 'Afternoon (1-4 PM)': 55, 'Evening (5-9 PM)': 160, 'Night (10 PM-12 AM)': 18},
    # ... (other data points)
    {'Date': '2023-03-12', 'Early Morning (5-8 AM)': 65, 'Late Morning (9 AM-12 PM)': 75, 'Afternoon (1-4 PM)': 70, 'Evening (5-9 PM)': 200, 'Night (10 PM-12 AM)': 30}
]

# Convert to a pandas DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set the Date as the index
df.set_index('Date', inplace=True)

# Plot
plt.figure(figsize=(12, 6))

# List of columns to plot
columns = ['Early Morning (5-8 AM)', 'Late Morning (9 AM-12 PM)', 'Afternoon (1-4 PM)', 'Evening (5-9 PM)', 'Night (10 PM-12 AM)']
# Reverse the order for correctly stacking
columns = columns[::-1]

# Prepare data for stacking by cumulating the values
cumulative = df[columns].cumsum(axis=1)
cumulative.insert(0, 'base', 0)  # Insert a base for starting point of the area chart

# We will create a color palette with Seaborn's color_palette()
palette = sns.color_palette("husl", len(columns))

# Iterate over the columns and fill the area between each
for i, column in enumerate(columns):
    plt.fill_between(df.index, cumulative.iloc[:, i], cumulative.iloc[:, i + 1], label=column, color=palette[i])
    sns.lineplot(x=df.index, y=cumulative.iloc[:, i], color=palette[i])

# Finalizing the plot
plt.title('Stacked Area Chart of Daily Time Segments')
plt.xlabel('Date')
plt.ylabel('Counts')
plt.xticks(rotation=45)
plt.legend(title='Time Segments', loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()

# Show the plot
plt.show()