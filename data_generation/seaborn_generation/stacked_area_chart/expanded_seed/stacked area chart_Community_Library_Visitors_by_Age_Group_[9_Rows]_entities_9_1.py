
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Given chart table data
data = [
    {'Date': '2023-02-01', 'Children (0-12)': 50, 'Teens (13-18)': 25, 'Adults (19-64)': 150, 'Seniors (65+)': 30},
    {'Date': '2023-02-02', 'Children (0-12)': 45, 'Teens (13-18)': 20, 'Adults (19-64)': 135, 'Seniors (65+)': 25},
    {'Date': '2023-02-03', 'Children (0-12)': 55, 'Teens (13-18)': 30, 'Adults (19-64)': 160, 'Seniors (65+)': 20},
    {'Date': '2023-02-04', 'Children (0-12)': 60, 'Teens (13-18)': 22, 'Adults (19-64)': 170, 'Seniors (65+)': 35},
    {'Date': '2023-02-05', 'Children (0-12)': 48, 'Teens (13-18)': 18, 'Adults (19-64)': 145, 'Seniors (65+)': 28},
    {'Date': '2023-02-06', 'Children (0-12)': 70, 'Teens (13-18)': 29, 'Adults (19-64)': 155, 'Seniors (65+)': 32},
    {'Date': '2023-02-07', 'Children (0-12)': 65, 'Teens (13-18)': 23, 'Adults (19-64)': 180, 'Seniors (65+)': 27},
    {'Date': '2023-02-08', 'Children (0-12)': 75, 'Teens (13-18)': 32, 'Adults (19-64)': 175, 'Seniors (65+)': 30},
    {'Date': '2023-02-09', 'Children (0-12)': 80, 'Teens (13-18)': 37, 'Adults (19-64)': 190, 'Seniors (65+)': 40}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Set the Date column as the index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Calculate cumulative data to stack the areas
cumulative_df = df.cumsum(axis=1)

# Use Seaborn to set the aesthetics
sns.set_style("whitegrid")

# Create the area plot
plt.stackplot(cumulative_df.index, cumulative_df.T, labels=cumulative_df.columns)

# Beautify the plot
plt.margins(0, 0)
plt.legend(loc='upper left')
plt.xticks(rotation=45)
plt.ylabel('Number of People')
plt.title('Visitor Numbers by Age Group Over Time')

# Show the plot
plt.show()