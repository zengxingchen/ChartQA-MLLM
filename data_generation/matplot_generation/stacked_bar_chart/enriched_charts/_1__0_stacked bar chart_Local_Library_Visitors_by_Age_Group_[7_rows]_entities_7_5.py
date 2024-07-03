
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Revenue (in millions)': [120, 150, 180, 200, 210, 230, 250, 270, 290, 300],
    'Expenses (in millions)': [80, 90, 100, 120, 130, 140, 160, 180, 190, 200],
    'Profit (in millions)': [20, 30, 40, 50, 55, 60, 70, 75, 80, 85],
    'Loss (in millions)': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
}

df = pd.DataFrame(data)

# Plotting the vertical stacked bar chart
fig, ax = plt.subplots(figsize=(12, 9))

ax.bar(df['Year'], df['Revenue (in millions)'], color='#1f77b4', edgecolor='grey', width=0.6, label='Revenue (in millions)')
ax.bar(df['Year'], df['Expenses (in millions)'], bottom=df['Revenue (in millions)'], color='#ff7f0e', edgecolor='grey', width=0.6, label='Expenses (in millions)')
ax.bar(df['Year'], df['Profit (in millions)'], bottom=df['Revenue (in millions)'] + df['Expenses (in millions)'], color='#2ca02c', edgecolor='grey', width=0.6, label='Profit (in millions)')
ax.bar(df['Year'], df['Loss (in millions)'], bottom=df['Revenue (in millions)'] + df['Expenses (in millions)'] + df['Profit (in millions)'], color='#d62728', edgecolor='grey', width=0.6, label='Loss (in millions)')

ax.set_ylabel('Amount in Millions')
ax.set_title('Company Financial Overview (2015-2024)', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

plt.show()