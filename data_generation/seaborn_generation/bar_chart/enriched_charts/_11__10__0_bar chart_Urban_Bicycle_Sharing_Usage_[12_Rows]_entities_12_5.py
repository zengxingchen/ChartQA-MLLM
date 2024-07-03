
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': ['2023-04-01', '2023-04-02', '2023-04-03', '2023-04-04', 
             '2023-04-05', '2023-04-06', '2023-04-07', '2023-04-08', 
             '2023-04-09', '2023-04-10', '2023-04-11', '2023-04-12', 
             '2023-04-13', '2023-04-14'],
    'Number of Tourists': [125, 135, 140, 155, 150, 165, 175, 185, 170, 155, 145, 160, 180, 195]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 10))
sns.barplot(y='Date', x='Number of Tourists', data=df,
            palette=['#4c72b0', '#55a868', '#c44e52', '#8172b2',
                     '#ccb974', '#64b5cd', '#8da0cb', '#e78ac3',
                     '#a6d854', '#ffd92f', '#e5c494', '#fc8d62',
                     '#66c2a5', '#e41a1c'],
            width=0.7,
            orient='h')

plt.ylabel('Date')
plt.xlabel('Number of Tourists')
plt.title('Two-week Tourist Visits in Fictitious City', pad=20)
sns.despine(left=True, bottom=True)

plt.show()