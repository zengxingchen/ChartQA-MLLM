
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data points from the given table
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Average Calorie Intake': [2100, 2150, 2200, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Create the line plot
plt.figure(figsize=(14, 7))  # Modify width and height
sns.lineplot(x='Year', y='Average Calorie Intake', data=df, color='#2ca02c')  # Change the color scheme

# Adding annotations for the start and end points
plt.text(2010, 2100, 'Start', horizontalalignment='left', size='small', color='black')
plt.text(2021, 2700, 'Latest', horizontalalignment='right', size='small', color='black')

# Setting the title and labels
plt.title('Annual Average Calorie Intake from 2010 to 2021', fontsize=16, loc='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Calorie Intake', fontsize=12)

sns.despine()
plt.show()