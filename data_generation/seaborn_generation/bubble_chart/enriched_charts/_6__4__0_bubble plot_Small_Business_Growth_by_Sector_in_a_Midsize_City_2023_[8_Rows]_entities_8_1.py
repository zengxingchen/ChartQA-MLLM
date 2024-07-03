
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
                'France', 'Brazil', 'Italy', 'Canada', 'Russia', 'South Korea', 
                'Spain', 'Australia', 'Mexico', 'Indonesia', 'Netherlands', 
                'Saudi Arabia', 'Turkey', 'Switzerland'],
    'Participation Rate (%)': [60, 45, 75, 65, 30, 62,
                               68, 50, 55, 72, 40, 75, 
                               67, 78, 35, 28, 69, 25, 
                               33, 80],
    'Average Weekly Exercise Hours': [5, 4, 6.5, 6, 3.5, 5.5,
                                      6, 4.5, 5, 7, 3.5, 6.5, 
                                      6, 7.5, 4, 3, 6.5, 2.5, 
                                      3.5, 7.5],
    'Population (Millions)': [331, 1438, 126, 83, 1367, 66,
                              65, 213, 60, 38, 145, 51,
                              47, 25, 128, 273, 17,
                              34, 84, 8],
    'Mental Health Index': [70, 65, 80, 75, 55, 72,
                            77, 60, 68, 85, 62, 80,
                            75, 88, 58, 50, 76, 45,
                            52, 90]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18, 14))
bubble_chart = sns.scatterplot(data=df,
                               x='Participation Rate (%)',
                               y='Average Weekly Exercise Hours',
                               size='Population (Millions)',
                               hue='Mental Health Index',
                               palette=['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0'],
                               sizes=(50, 1000),
                               alpha=0.7)

plt.title('Mental Health Indicators of Different Countries', fontsize=20, loc='center')
plt.xlabel('Participation Rate (%)', fontsize=14)
plt.ylabel('Average Weekly Exercise Hours', fontsize=14)
plt.legend(loc='upper left', title='Population (Millions)')

plt.show()