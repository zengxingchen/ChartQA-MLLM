
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Drama': [70, 60, 80, 90, 85, 75, 65, 95, 70, 85, 90, 75],
    'Comedy': [50, 65, 55, 60, 70, 80, 85, 75, 90, 95, 85, 60],
    'Action': [60, 70, 75, 65, 80, 90, 95, 85, 80, 75, 70, 65],
    'Documentary': [20, 15, 30, 25, 40, 35, 45, 50, 55, 60, 65, 70]
}

df = pd.DataFrame(data)

df_percentage = df.copy()
df_percentage['Drama'] = df['Drama'] / df[['Drama', 'Comedy', 'Action', 'Documentary']].sum(axis=1) * 100
df_percentage['Comedy'] = df['Comedy'] / df[['Drama', 'Comedy', 'Action', 'Documentary']].sum(axis=1) * 100
df_percentage['Action'] = df['Action'] / df[['Drama', 'Comedy', 'Action', 'Documentary']].sum(axis=1) * 100
df_percentage['Documentary'] = df['Documentary'] / df[['Drama', 'Comedy', 'Action', 'Documentary']].sum(axis=1) * 100

categories = df_percentage['Month']
N = len(categories)
ind = np.arange(N)
width = 0.5

colors = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a']

plt.figure(figsize=(10, 8))
plt.bar(ind, df_percentage['Drama'], width=width, color=colors[0], label='Drama')
plt.bar(ind, df_percentage['Comedy'], width=width, bottom=df_percentage['Drama'], color=colors[1], label='Comedy')
plt.bar(ind, df_percentage['Action'], width=width, bottom=df_percentage['Drama'] + df_percentage['Comedy'], color=colors[2], label='Action')
plt.bar(ind, df_percentage['Documentary'], width=width, bottom=df_percentage['Drama'] + df_percentage['Comedy'] + df_percentage['Action'], color=colors[3], label='Documentary')

plt.title('Monthly Streaming Preferences (%)')
plt.ylabel('Percentage')
plt.xticks(ind, categories, rotation=45)
plt.ylim(0, 100)
plt.legend(loc='upper right')

plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.25)

plt.show()