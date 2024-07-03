
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Country': ['France', 'Spain', 'United States', 'China', 'Italy', 'Turkey', 'Mexico', 'Thailand', 'Germany', 'United Kingdom',
                'Japan', 'Austria', 'Greece', 'Russia', 'Canada', 'Portugal', 'Netherlands', 'Saudi Arabia', 'Switzerland', 'South Korea'],
    'Visitors per Year (Millions)': [89.4, 83.7, 79.3, 65.7, 64.5, 51.2, 45.0, 39.8, 38.9, 36.3,
                                     31.2, 30.8, 30.1, 28.5, 22.1, 21.2, 20.0, 19.2, 18.4, 17.5],
    'Attraction Rating (Stars)': [4.7, 4.5, 4.8, 4.2, 4.6, 4.1, 4.3, 4.4, 4.5, 4.7,
                                  4.6, 4.2, 4.3, 4.0, 4.7, 4.5, 4.4, 4.1, 4.6, 4.3],
    'Population (Millions)': [65, 47, 331, 1438, 60, 84, 128, 70, 83, 66,
                              126, 9, 10, 145, 38, 10, 17, 34, 8, 51]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=df,
                               x='Visitors per Year (Millions)',
                               y='Attraction Rating (Stars)',
                               size='Population (Millions)',
                               hue='Visitors per Year (Millions)',
                               palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'],
                               sizes=(100, 2000),
                               alpha=0.7)

plt.title('Tourism Popularity and Attraction Ratings')
plt.xlabel('Visitors per Year (Millions)')
plt.ylabel('Attraction Rating (Stars)')
plt.legend(loc='upper right', title='Population (Millions)')
plt.show()