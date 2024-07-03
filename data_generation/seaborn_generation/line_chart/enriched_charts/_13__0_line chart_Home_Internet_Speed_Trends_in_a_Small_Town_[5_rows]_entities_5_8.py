
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data points from the given table
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Average Exam Scores': [78, 80, 77, 82, 79, 85, 83, 88, 86, 87, 90, 92]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Create the line plot
plt.figure(figsize=(14, 7))  # Modify width and height
sns.lineplot(x='Year', y='Average Exam Scores', data=df, color='#FF5733')  # Change the color scheme

# Adding annotations for the start and end points
plt.text(2010, 78, 'Start', horizontalalignment='left', size='small', color='black')
plt.text(2021, 92, 'Latest', horizontalalignment='right', size='small', color='black')

# Setting the title and labels
plt.title('Annual Average Exam Scores from 2010 to 2021', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Exam Scores', fontsize=12)

sns.despine()
plt.show()