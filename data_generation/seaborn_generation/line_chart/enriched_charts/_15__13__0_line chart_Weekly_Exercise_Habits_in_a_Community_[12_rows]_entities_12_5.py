
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Prepare the data
data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Average Marathon Time (hours)': [4.2, 4.1, 4.0, 4.3, 4.4, 4.2, 4.3, 4.5, 4.6, 4.8, 4.7]
}

df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 6))

# Plot the data
sns.lineplot(data=df, x='Year', y='Average Marathon Time (hours)', color='#1f77b4', linewidth=2.5)

# Customizing the axes and ticks
ax.set(xlim=(2010, 2022), xlabel='Year', ylabel='Average Marathon Time (hours)')
ax.set_title('Average Marathon Finishing Times Over the Years', pad=20)

# Annotations
for x, y in zip(df['Year'], df['Average Marathon Time (hours)']):
    ax.text(x, y, f'{y}h', color='black', ha="center", va="bottom")

# Show the plot
plt.show()