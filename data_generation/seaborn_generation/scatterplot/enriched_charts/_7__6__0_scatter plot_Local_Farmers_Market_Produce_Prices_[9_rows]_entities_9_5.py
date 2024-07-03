
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

data = '''
Date,NumberOfArticles,ReadingTime
2023-01-01,8,25
2023-01-02,7,23
2023-01-03,10,30
2023-01-04,12,35
2023-01-05,8.5,26
2023-01-06,9,28
2023-01-07,9.5,29
2023-01-08,11,32
2023-01-09,9.8,30.5
2023-01-10,8.7,27
2023-01-11,11.5,34
2023-01-12,8,25
2023-01-13,10.5,31
2023-01-14,7,22
2023-01-15,8.5,26
2023-01-16,13,38
2023-01-17,8.2,24.5
2023-01-18,7.6,23.5
2023-01-19,9.2,27.5
2023-01-20,8.9,26.5
2023-01-21,12.1,36
2023-01-22,10.8,32.5
2023-01-23,11.2,33.5
2023-01-24,10,31.5
2023-01-25,9.4,28.5
2023-01-26,11.7,34.5
2023-01-27,12.3,35.5
2023-01-28,7.9,24
2023-01-29,9.6,29
2023-01-30,8.1,25.5
2023-01-31,11.4,33
'''

df = pd.read_csv(StringIO(data), parse_dates=['Date'])

plt.figure(figsize=(18, 12))

sns.scatterplot(data=df, x='Date', y='NumberOfArticles', size='ReadingTime',
                sizes=(20, 200), hue='ReadingTime', palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

plt.title('Monthly Reading Habit: Number of Articles vs Reading Time', fontsize=22, pad=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Number of Articles', fontsize=16)

plt.show()