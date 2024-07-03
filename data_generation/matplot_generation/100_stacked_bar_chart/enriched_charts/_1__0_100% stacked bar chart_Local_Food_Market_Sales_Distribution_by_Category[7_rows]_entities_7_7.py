import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Solar': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'Wind': [30, 35, 25, 30, 20, 25, 20, 15, 15, 10],
    'Hydro': [40, 30, 35, 25, 30, 20, 20, 20, 15, 15],
    'Geothermal': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
}

df = pd.DataFrame(data)

# Normalize the data to 100% for stacking
totals = df.iloc[:, 1:].sum(axis=1)
df_normalized = df.copy()
df_normalized.iloc[:, 1:] = df.iloc[:, 1:].div(totals, 0) * 100

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.4

ax.barh(df['Year'], df_normalized['Solar'], color='#FF5733', edgecolor='white', height=bar_width, label='Solar')
ax.barh(df['Year'], df_normalized['Wind'], left=df_normalized['Solar'], color='#33FF57', edgecolor='white', height=bar_width, label='Wind')
ax.barh(df['Year'], df_normalized['Hydro'], left=df_normalized['Solar'] + df_normalized['Wind'], color='#3357FF', edgecolor='white', height=bar_width, label='Hydro')
ax.barh(df['Year'], df_normalized['Geothermal'], left=df_normalized['Solar'] + df_normalized['Wind'] + df_normalized['Hydro'], color='#FF33FF', edgecolor='white', height=bar_width, label='Geothermal')

# Title and labels
ax.set_title('Renewable Energy Sources (2015-2024)', fontsize=14)
ax.set_xlabel('Percentage (%)', fontsize=12)
ax.set_ylabel('Year', fontsize=12)
ax.legend(loc='upper right')

plt.show()