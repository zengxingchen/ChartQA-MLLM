
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Prepare the data
data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Awareness Index': [40, 45, 47, 50, 55, 60, 62, 68, 70, 75, 80]
}

df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 6))

# Plot the data
sns.lineplot(data=df, x='Year', y='Awareness Index', color='#ff5733', linewidth=2.5)

# Customizing the axes and ticks
ax.set(xlim=(2010, 2022), xlabel='Year', ylabel='Awareness Index')
ax.set_title('Annual Increase in Mental Health Awareness', fontsize=16)

# Annotations
for x, y in zip(df['Year'], df['Awareness Index']):
    ax.text(x, y, f'{y}', color='black', ha="center")

# Show the plot
plt.show()