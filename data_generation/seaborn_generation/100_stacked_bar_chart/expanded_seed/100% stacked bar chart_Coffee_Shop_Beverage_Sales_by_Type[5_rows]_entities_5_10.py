
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime

# Convert the table data to a DataFrame
data = [
    {'Date': '2023-01-01', 'Espresso Based': '30%', 'Filtered Coffee': '25%', 'Tea': '20%', 'Smoothies': '15%', 'Soft Drinks': '10%'},
    {'Date': '2023-02-01', 'Espresso Based': '35%', 'Filtered Coffee': '20%', 'Tea': '20%', 'Smoothies': '15%', 'Soft Drinks': '10%'},
    {'Date': '2023-03-01', 'Espresso Based': '40%', 'Filtered Coffee': '18%', 'Tea': '17%', 'Smoothies': '15%', 'Soft Drinks': '10%'},
    {'Date': '2023-04-01', 'Espresso Based': '42%', 'Filtered Coffee': '20%', 'Tea': '15%', 'Smoothies': '13%', 'Soft Drinks': '10%'},
    {'Date': '2023-05-01', 'Espresso Based': '30%', 'Filtered Coffee': '25%', 'Tea': '25%', 'Smoothies': '10%', 'Soft Drinks': '10%'}
]

df = pd.DataFrame(data)

# Transform percentage strings into numbers
for col in df.columns:
    if col != 'Date':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

# Pivot the data to long format
df_long = df.melt(id_vars='Date', var_name='Beverage', value_name='Percentage')

# Sort the DataFrame based on Date to maintain the order
df_long['Date'] = pd.to_datetime(df_long['Date'])
df_long.sort_values(by='Date', inplace=True)

# Plotting the 100% stacked bar chart
categories = df.columns[1:]
colors = sns.color_palette('pastel', len(categories))

# Starting point for the first category
left = len(df_long['Date'].unique()) * [0]

fig, ax = plt.subplots(figsize=(10, 6))

# Iterate through the beverage categories
for ix, category in enumerate(categories):
    category_data = df_long[df_long['Beverage'] == category]
    plt.bar(
        category_data['Date'].dt.strftime('%Y-%m-%d'),
        category_data['Percentage'],
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
plt.title('Sales Distribution by Beverage Type over Time')
plt.legend(title='Beverage', bbox_to_anchor=(1.05, 1), loc='upper left')

# Make it tight layout to fit the legend
plt.tight_layout()

# Display the plot
plt.show()