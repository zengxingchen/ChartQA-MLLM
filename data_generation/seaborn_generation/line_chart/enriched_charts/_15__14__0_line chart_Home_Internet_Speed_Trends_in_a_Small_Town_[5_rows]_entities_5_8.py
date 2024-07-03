
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data points for the new topic
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Average Monthly Rainfall (mm)': [120, 130, 115, 140, 150, 135, 145, 160, 155, 170, 180, 175]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Create the line plot
plt.figure(figsize=(16, 8))  # Modify width and height
sns.lineplot(x='Year', y='Average Monthly Rainfall (mm)', data=df, color='#1f77b4')  # Change the color scheme

# Adding annotations for the start and end points
plt.text(2010, 120, 'Start', horizontalalignment='left', size='medium', color='black')
plt.text(2021, 175, 'End', horizontalalignment='right', size='medium', color='black')

# Setting the title and labels
plt.title('Annual Average Monthly Rainfall from 2010 to 2021', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Monthly Rainfall (mm)', fontsize=14)

sns.despine()
plt.show()