
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Distance Covered (in km)': [100, 120, 150, 180, 210, 240, 270, 300, 330, 360],
    'Calories Burned': [500, 600, 750, 900, 1050, 1200, 1350, 1500, 1650, 1800],
    'Average Speed (in km/h)': [10, 12, 15, 18, 21, 24, 27, 30, 33, 36],
    'Time Spent (in hours)': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
}

df = pd.DataFrame(data)

# Plotting the horizontal stacked bar chart
fig, ax = plt.subplots(figsize=(14, 8))

ax.barh(df['Year'], df['Distance Covered (in km)'], color='#1e90ff', edgecolor='grey', height=0.4, label='Distance Covered (in km)')
ax.barh(df['Year'], df['Calories Burned'], left=df['Distance Covered (in km)'], color='#ff4500', edgecolor='grey', height=0.4, label='Calories Burned')
ax.barh(df['Year'], df['Average Speed (in km/h)'], left=df['Distance Covered (in km)'] + df['Calories Burned'], color='#32cd32', edgecolor='grey', height=0.4, label='Average Speed (in km/h)')
ax.barh(df['Year'], df['Time Spent (in hours)'], left=df['Distance Covered (in km)'] + df['Calories Burned'] + df['Average Speed (in km/h)'], color='#8a2be2', edgecolor='grey', height=0.4, label='Time Spent (in hours)')

for index, row in df.iterrows():
    ax.text(row['Distance Covered (in km)']/2, index, str(row['Distance Covered (in km)']), color='black', va='center', ha='center')
    ax.text(row['Distance Covered (in km)'] + row['Calories Burned']/2, index, str(row['Calories Burned']), color='black', va='center', ha='center')
    ax.text(row['Distance Covered (in km)'] + row['Calories Burned'] + row['Average Speed (in km/h)']/2, index, str(row['Average Speed (in km/h)']), color='black', va='center', ha='center')
    ax.text(row['Distance Covered (in km)'] + row['Calories Burned'] + row['Average Speed (in km/h)'] + row['Time Spent (in hours)']/2, index, str(row['Time Spent (in hours)']), color='black', va='center', ha='center')

ax.set_xlabel('Amount')
ax.set_title('Annual Fitness Activity Overview (2015-2024)', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1))

plt.show()