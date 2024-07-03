
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Your provided data
data = [
    {'Year': 2018, "Children's Books": 5500, 'Young Adult Books': 3000, 'Adult Fiction': 7000, 'Adult Non-fiction': 4500, 'Reference Works': 2000},
    {'Year': 2019, "Children's Books": 5800, 'Young Adult Books': 3200, 'Adult Fiction': 7300, 'Adult Non-fiction': 4600, 'Reference Works': 1800},
    {'Year': 2020, "Children's Books": 4000, 'Young Adult Books': 2800, 'Adult Fiction': 6900, 'Adult Non-fiction': 4700, 'Reference Works': 1500},
    {'Year': 2021, "Children's Books": 4200, 'Young Adult Books': 3000, 'Adult Fiction': 7100, 'Adult Non-fiction': 4800, 'Reference Works': 1400},
    {'Year': 2022, "Children's Books": 4300, 'Young Adult Books': 3100, 'Adult Fiction': 7200, 'Adult Non-fiction': 4900, 'Reference Works': 1300},
    {'Year': 2023, "Children's Books": 4500, 'Young Adult Books': 3300, 'Adult Fiction': 7400, 'Adult Non-fiction': 5000, 'Reference Works': 1200}
]

# Transform the data into a long-form DataFrame
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
df_long = df.stack().reset_index()
df_long.columns = ['Year', 'Category', 'Sales']

# Pivot the DataFrame to have Years as index and categories as columns, and sales values as data
df_pivot = df_long.pivot(index='Year', columns='Category', values='Sales')

# Sort the columns if necessary
order = df_pivot.mean().sort_values().index

# Use Seaborn to set the aesthetic appearance
sns.set_theme(style='whitegrid')

# Use matplotlib to plot the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(df_pivot.index, df_pivot[order].T, labels=order)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Book Sales by Category Over Time')

# Add legend
ax.legend(loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()