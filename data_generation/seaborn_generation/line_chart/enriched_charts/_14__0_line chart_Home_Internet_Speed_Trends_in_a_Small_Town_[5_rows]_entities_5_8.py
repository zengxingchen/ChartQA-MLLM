
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data points for the new topic
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Average Running Distance (km)': [250, 265, 280, 300, 320, 310, 330, 340, 360, 375, 390, 410]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Create the line plot
plt.figure(figsize=(14, 7))  # Modify width and height
sns.lineplot(x='Year', y='Average Running Distance (km)', data=df, color='#ff7f0e')  # Change the color scheme

# Adding annotations for the start and end points
plt.text(2010, 250, 'Start', horizontalalignment='left', size='medium', color='black')
plt.text(2021, 410, 'Latest', horizontalalignment='right', size='medium', color='black')

# Setting the title and labels
plt.title('Annual Average Running Distance from 2010 to 2021', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Running Distance (km)', fontsize=14)

sns.despine()
plt.show()