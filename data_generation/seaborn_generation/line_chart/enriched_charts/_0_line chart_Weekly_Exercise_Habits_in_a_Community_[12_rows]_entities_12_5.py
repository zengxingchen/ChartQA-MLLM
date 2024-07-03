
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Prepare the data
data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Electric Car Sales': [50, 100, 150, 300, 400, 550, 700, 900, 1100, 1400, 1700]
}

df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 6))

# Plot the data
sns.lineplot(data=df, x='Year', y='Electric Car Sales', color='#1f77b4', linewidth=2.5)

# Customizing the axes and ticks
ax.set(xlim=(2010, 2022), xlabel='Year', ylabel='Sales (in thousands)')
ax.set_title('Electric Car Sales Over Time')

# Annotations
for x, y in zip(df['Year'], df['Electric Car Sales']):
    ax.text(x, y, f'{y}', color='black', ha="center")

# Show the plot
plt.show()