
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Given data
data = [
    {'Year': 2016, 'Parks': 10, 'Sports Fields': 5, 'Gardens': 7, 'Playgrounds': 4},
    {'Year': 2017, 'Parks': 11, 'Sports Fields': 5, 'Gardens': 8, 'Playgrounds': 4},
    {'Year': 2018, 'Parks': 12, 'Sports Fields': 6, 'Gardens': 9, 'Playgrounds': 5},
    {'Year': 2019, 'Parks': 12, 'Sports Fields': 7, 'Gardens': 10, 'Playgrounds': 6},
    {'Year': 2020, 'Parks': 13, 'Sports Fields': 7, 'Gardens': 11, 'Playgrounds': 7}
]

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data)

# Set the style
sns.set_style('whitegrid')

# Prepare data for the stackplot
x = df['Year'].values
y_arrays = [df['Parks'].values, df['Sports Fields'].values, df['Gardens'].values, df['Playgrounds'].values]
y_cum = np.cumsum(y_arrays, axis=0)

fig, ax = plt.subplots()

# Plot the stackplot
ax.stackplot(x, y_arrays, labels=['Parks', 'Sports Fields', 'Gardens', 'Playgrounds'], 
             colors=sns.color_palette('pastel'), alpha=0.8)

# Adding labels, title, and legend
ax.set_title('Community Asset Distribution Over Years')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Assets')
ax.legend(loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()