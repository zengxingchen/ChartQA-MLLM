
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime

# Convert the table data to a DataFrame
data = [
    {'Date': '2023-01-01', 'Exercise': '30%', 'Healthy Eating': '20%', 'Mental Health Activities': '15%', 'Socializing': '25%', 'Sleep': '10%'},
    {'Date': '2023-02-01', 'Exercise': '28%', 'Healthy Eating': '22%', 'Mental Health Activities': '18%', 'Socializing': '22%', 'Sleep': '10%'},
    {'Date': '2023-03-01', 'Exercise': '25%', 'Healthy Eating': '25%', 'Mental Health Activities': '20%', 'Socializing': '20%', 'Sleep': '10%'},
    {'Date': '2023-04-01', 'Exercise': '27%', 'Healthy Eating': '23%', 'Mental Health Activities': '19%', 'Socializing': '21%', 'Sleep': '10%'},
    {'Date': '2023-05-01', 'Exercise': '30%', 'Healthy Eating': '22%', 'Mental Health Activities': '18%', 'Socializing': '20%', 'Sleep': '10%'},
    {'Date': '2023-06-01', 'Exercise': '32%', 'Healthy Eating': '20%', 'Mental Health Activities': '15%', 'Socializing': '23%', 'Sleep': '10%'}
]

df = pd.DataFrame(data)

# Transform percentage strings into numbers
for col in df.columns:
    if col != 'Date':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

# Pivot the data to long format
df_long = df.melt(id_vars='Date', var_name='Activity', value_name='Percentage')

# Sort the DataFrame based on Date to maintain the order
df_long['Date'] = pd.to_datetime(df_long['Date'])
df_long.sort_values(by='Date', inplace=True)

# Plotting the 100% stacked bar chart
categories = df.columns[1:]
colors = ['#3498DB', '#2ECC71', '#E74C3C', '#F1C40F', '#9B59B6']

# Starting point for the first category
left = len(df_long['Date'].unique()) * [0]

fig, ax = plt.subplots(figsize=(14, 10))

# Iterate through the activity categories
for ix, category in enumerate(categories):
    category_data = df_long[df_long['Activity'] == category]
    plt.bar(
        category_data['Date'].dt.strftime('%Y-%m-%d'),
        category_data['Percentage'],
        width=0.8,
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
plt.title('Health Activity Distribution Over Time')
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Make it tight layout to fit the legend
plt.tight_layout()

# Display the plot
plt.show()