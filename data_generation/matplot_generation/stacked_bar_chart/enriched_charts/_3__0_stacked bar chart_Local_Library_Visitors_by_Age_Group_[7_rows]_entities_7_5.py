
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020],
    'Books': [50, 45, 55, 60, 65, 70],
    'Magazines': [30, 35, 28, 33, 40, 42],
    'Newspapers': [20, 25, 22, 30, 28, 35],
    'Comics': [10, 15, 20, 25, 30, 35]
}

df = pd.DataFrame(data)

# Plotting the vertical stacked bar chart
fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(df['Year'], df['Books'], color='#8B0000', edgecolor='grey', width=0.6, label='Books')
ax.bar(df['Year'], df['Magazines'], bottom=df['Books'], color='#FF8C00', edgecolor='grey', width=0.6, label='Magazines')
ax.bar(df['Year'], df['Newspapers'], bottom=df['Books']+df['Magazines'], color='#4682B4', edgecolor='grey', width=0.6, label='Newspapers')
ax.bar(df['Year'], df['Comics'], bottom=df['Books']+df['Magazines']+df['Newspapers'], color='#32CD32', edgecolor='grey', width=0.6, label='Comics')

for i, year in enumerate(df['Year']):
    total = df['Books'][i] + df['Magazines'][i] + df['Newspapers'][i] + df['Comics'][i]
    ax.text(year, total + 2, str(total), ha='center', va='bottom')

ax.set_ylabel('Quantity of Publications')
ax.set_xlabel('Year')
ax.set_title('Publication Consumption Over Years')
ax.legend(loc='upper left')

plt.show()