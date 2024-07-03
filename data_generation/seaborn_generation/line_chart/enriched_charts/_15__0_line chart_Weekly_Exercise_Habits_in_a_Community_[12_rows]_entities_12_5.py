
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Prepare the data
data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Number of Tourists': [120, 200, 320, 450, 620, 500, 780, 900, 870, 550, 950]
}

df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(14, 8))

# Plot the data
sns.lineplot(data=df, x='Year', y='Number of Tourists', color='#ff6347', linewidth=2.5)

# Customizing the axes and ticks
ax.set(xlim=(2010, 2022), xlabel='Year', ylabel='Number of Tourists (in thousands)')
ax.set_title('Tourism Trends Over the Decade')

# Annotations
for x, y in zip(df['Year'], df['Number of Tourists']):
    ax.text(x, y, f'{y}', color='black', ha="center")

# Show the plot
plt.show()