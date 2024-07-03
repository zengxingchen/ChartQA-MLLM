
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data points from the given table
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'CO2 Emissions': [33.1, 34.0, 35.2, 36.4, 37.0, 37.5, 36.8, 36.5, 37.2, 37.5, 36.0, 37.1]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Create the line plot
plt.figure(figsize=(14, 7))  # Modify width and height
sns.lineplot(x='Year', y='CO2 Emissions', data=df, color='#FF5733')  # Change the color scheme

# Adding annotations for the start and end points
plt.text(2010, 33.1, 'Start', horizontalalignment='left', size='small', color='black')
plt.text(2021, 37.1, 'Latest', horizontalalignment='right', size='small', color='black')

# Setting the title and labels
plt.title('Annual CO2 Emissions from 2010 to 2021', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('CO2 Emissions (MtCO2)', fontsize=12)

sns.despine()
plt.show()