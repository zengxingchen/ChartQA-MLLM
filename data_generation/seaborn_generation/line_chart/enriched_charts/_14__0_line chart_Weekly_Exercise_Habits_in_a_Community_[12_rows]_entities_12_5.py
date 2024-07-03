
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Prepare the data
data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Population Growth Rate': [1.2, 1.3, 1.5, 1.4, 1.6, 1.7, 1.5, 1.8, 2.0, 1.9, 2.1]
}

df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 5))

# Plot the data
sns.lineplot(data=df, x='Year', y='Population Growth Rate', color='#ff7f0e', linewidth=2.5)

# Customizing the axes and ticks
ax.set(xlim=(2010, 2022), xlabel='Year', ylabel='Growth Rate (%)')
ax.set_title('Population Growth Rate Over Time', pad=20)

# Annotations
for x, y in zip(df['Year'], df['Population Growth Rate']):
    ax.text(x, y, f'{y}%', color='black', ha="center")

# Show the plot
plt.show()