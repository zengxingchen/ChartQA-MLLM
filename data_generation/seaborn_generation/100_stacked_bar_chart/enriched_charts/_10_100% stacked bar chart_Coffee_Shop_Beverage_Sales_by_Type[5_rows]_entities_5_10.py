
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime

# Convert the table data to a DataFrame
data = [
    {'Date': '2023-01-01', 'Pop': '25%', 'Rock': '30%', 'Jazz': '20%', 'Classical': '15%', 'Hip Hop': '10%'},
    {'Date': '2023-02-01', 'Pop': '28%', 'Rock': '25%', 'Jazz': '22%', 'Classical': '15%', 'Hip Hop': '10%'},
    {'Date': '2023-03-01', 'Pop': '30%', 'Rock': '22%', 'Jazz': '18%', 'Classical': '20%', 'Hip Hop': '10%'},
    {'Date': '2023-04-01', 'Pop': '32%', 'Rock': '20%', 'Jazz': '18%', 'Classical': '20%', 'Hip Hop': '10%'},
    {'Date': '2023-05-01', 'Pop': '35%', 'Rock': '20%', 'Jazz': '15%', 'Classical': '20%', 'Hip Hop': '10%'},
    {'Date': '2023-06-01', 'Pop': '33%', 'Rock': '21%', 'Jazz': '17%', 'Classical': '19%', 'Hip Hop': '10%'}
]

df = pd.DataFrame(data)

# Transform percentage strings into numbers
for col in df.columns:
    if col != 'Date':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

# Pivot the data to long format
df_long = df.melt(id_vars='Date', var_name='Genre', value_name='Percentage')

# Sort the DataFrame based on Date to maintain the order
df_long['Date'] = pd.to_datetime(df_long['Date'])
df_long.sort_values(by='Date', inplace=True)

# Plotting the 100% stacked bar chart
categories = df.columns[1:]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF']

# Starting point for the first category
left = len(df_long['Date'].unique()) * [0]

fig, ax = plt.subplots(figsize=(12, 8))

# Iterate through the genre categories
for ix, category in enumerate(categories):
    category_data = df_long[df_long['Genre'] == category]
    plt.bar(
        category_data['Date'].dt.strftime('%Y-%m-%d'),
        category_data['Percentage'],
        width=0.6,
        bottom=left,
        color=colors[ix],
        edgecolor="white",
        label=category
    )
    # Add the current category to 'left' for the next series
    left = left + category_data['Percentage'].values

# Customizations
plt.xticks(rotation=45)
plt.yticks(ticks=[0, 0.25, 0.5, 0.75, 1], labels=['0%', '25%', '50%', '75%', '100%'])
plt.ylabel('Percentage')
plt.title('Music Genre Popularity Distribution Over Time')
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')

# Make it tight layout to fit the legend
plt.tight_layout()

# Display the plot
plt.show()