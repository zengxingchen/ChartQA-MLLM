
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Institution': ['Team A', 'Team A', 'Team A', 'Team A', 'Team A',
                    'Team B', 'Team B', 'Team B', 'Team B', 'Team B',
                    'Team C', 'Team C', 'Team C', 'Team C', 'Team C',
                    'Team D', 'Team D', 'Team D', 'Team D', 'Team D',
                    'Team E', 'Team E', 'Team E', 'Team E', 'Team E'],
    'Year': [2018, 2019, 2020, 2021, 2022,
             2018, 2019, 2020, 2021, 2022,
             2018, 2019, 2020, 2021, 2022,
             2018, 2019, 2020, 2021, 2022,
             2018, 2019, 2020, 2021, 2022],
    'Points Scored': [85, 90, 88, 92, 95,
                      78, 85, 83, 87, 91,
                      80, 82, 84, 89, 93,
                      88, 90, 92, 95, 97,
                      82, 86, 89, 91, 94]
}

df = pd.DataFrame(data)
pivot_df = df.pivot(index='Year', columns='Institution', values='Points Scored')

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
pivot_df.plot(kind='bar', stacked=True, color=colors, width=0.6, figsize=(12, 8))

plt.title('Points Scored by Teams (2018-2022)', pad=20)
plt.xlabel('Year', labelpad=15)
plt.ylabel('Points Scored', labelpad=15)
plt.legend(title='Institution', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.savefig('points_scored_stacked_bar.png')
plt.show()