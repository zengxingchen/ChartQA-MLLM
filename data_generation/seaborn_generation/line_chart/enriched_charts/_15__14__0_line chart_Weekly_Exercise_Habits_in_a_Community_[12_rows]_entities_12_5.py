
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Prepare the data
data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Inflation Rate (%)': [3.2, 2.7, 2.5, 1.9, 0.7, 1.3, 2.1, 2.4, 1.8, 1.2, 2.5]
}

df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 6))

# Plot the data
sns.lineplot(data=df, x='Year', y='Inflation Rate (%)', color='#1f77b4', linewidth=2.5)

# Customizing the axes and ticks
ax.set(xlim=(2010, 2022), xlabel='Year', ylabel='Inflation Rate (%)')
ax.set_title('Inflation Rate Over Time', pad=20)

# Annotations
for x, y in zip(df['Year'], df['Inflation Rate (%)']):
    ax.text(x, y, f'{y}%', color='black', ha="center")

# Show the plot
plt.show()