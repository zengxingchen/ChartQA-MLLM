
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given data
data = [
    {'Year': 2008, 'Coal': 320, 'Natural Gas': 140, 'Renewables': 60, 'Nuclear': 100, 'Other': 20},
    {'Year': 2009, 'Coal': 300, 'Natural Gas': 150, 'Renewables': 70, 'Nuclear': 100, 'Other': 25},
    {'Year': 2010, 'Coal': 280, 'Natural Gas': 160, 'Renewables': 85, 'Nuclear': 95, 'Other': 30},
    {'Year': 2011, 'Coal': 260, 'Natural Gas': 165, 'Renewables': 95, 'Nuclear': 90, 'Other': 35},
    {'Year': 2012, 'Coal': 240, 'Natural Gas': 170, 'Renewables': 110, 'Nuclear': 85, 'Other': 40},
    {'Year': 2013, 'Coal': 220, 'Natural Gas': 180, 'Renewables': 125, 'Nuclear': 80, 'Other': 45},
    {'Year': 2014, 'Coal': 200, 'Natural Gas': 190, 'Renewables': 140, 'Nuclear': 78, 'Other': 50},
    {'Year': 2015, 'Coal': 180, 'Natural Gas': 195, 'Renewables': 155, 'Nuclear': 75, 'Other': 55},
    {'Year': 2016, 'Coal': 160, 'Natural Gas': 200, 'Renewables': 170, 'Nuclear': 70, 'Other': 58},
    {'Year': 2017, 'Coal': 140, 'Natural Gas': 210, 'Renewables': 185, 'Nuclear': 65, 'Other': 60},
    {'Year': 2018, 'Coal': 120, 'Natural Gas': 220, 'Renewables': 200, 'Nuclear': 60, 'Other': 62},
    {'Year': 2019, 'Coal': 100, 'Natural Gas': 230, 'Renewables': 220, 'Nuclear': 58, 'Other': 64},
    {'Year': 2020, 'Coal': 80, 'Natural Gas': 240, 'Renewables': 240, 'Nuclear': 55, 'Other': 66}
]

# Convert dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# To create a stacked area chart, we need the cumulative sum in reverse order
df = df.set_index('Year')
df_cumsum = df.iloc[:, ::-1].cumsum(axis=1).iloc[:, ::-1]

# Plot the areas using seaborn and matplotlib
sns.set(style="whitegrid")

fig, ax = plt.subplots(figsize=(10, 6))

# Define the palette to use
palette = sns.color_palette("husl", len(df.columns))

# Plot each column as a line and fill the area under it
for i, column in enumerate(df_cumsum.columns):
    sns.lineplot(data=df_cumsum, x=df_cumsum.index, y=column, color=palette[i])
    ax.fill_between(df_cumsum.index, df_cumsum[column], color=palette[i], alpha=0.4)

# Customize the plot
ax.set_ylabel("Energy Production")
ax.set_xlabel("Year")
ax.set_title("Energy Production by Source Over Time")
plt.legend(labels=df.columns, loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()