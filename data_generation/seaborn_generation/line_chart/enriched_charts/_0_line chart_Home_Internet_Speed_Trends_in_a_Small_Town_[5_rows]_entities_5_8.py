
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data points from the given table
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'GDP Growth': [2.5, 1.6, 2.2, 1.7, 2.6, 2.9, 1.6, 2.4, 2.9, 2.3, -3.5, 5.7]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Create the line plot
plt.figure(figsize=(12, 6))  # Modify width and height
sns.lineplot(x='Year', y='GDP Growth', data=df, color='#1f77b4')  # Change the color scheme

# Adding annotations for the start and end points
plt.text(2010, 2.5, 'Start', horizontalalignment='left', size='small', color='black')
plt.text(2021, 5.7, 'Latest', horizontalalignment='right', size='small', color='black')

# Setting the title and labels
plt.title('Annual GDP Growth from 2010 to 2021', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('GDP Growth (%)', fontsize=12)

sns.despine()
plt.show()