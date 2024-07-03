
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Prepare the data
data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'GDP Growth Rate': [2.0, 2.5, 1.8, 3.0, 2.8, 1.5, 2.2, 2.9, 2.3, -3.5, 5.0]
}

df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 5))

# Plot the data
sns.lineplot(data=df, x='Year', y='GDP Growth Rate', color='#2ca02c', linewidth=2.5)

# Customizing the axes and ticks
ax.set(xlim=(2010, 2022), xlabel='Year', ylabel='GDP Growth Rate (%)')
ax.set_title('Annual GDP Growth Rate Over Time')

# Annotations
for x, y in zip(df['Year'], df['GDP Growth Rate']):
    ax.text(x, y, f'{y}%', color='black', ha="center")

# Show the plot
plt.show()