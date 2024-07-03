
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
             'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
             'Fort Worth', 'Columbus', 'Charlotte'],
    'number_of_bookstores': [247, 189, 156, 97, 85, 104, 63, 72, 83, 58, 61, 47, 53, 68, 71]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
barplot = sns.barplot(
    x='number_of_bookstores',
    y='city',
    data=df,
    palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22',
             '#17becf', '#9edae5', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#c49c94'],
    orient='h'
)

for bar in barplot.patches:
    bar.set_height(0.7)

plt.title('Number of Bookstores in Major US Cities', fontsize=18, pad=15)
plt.xlabel('Number of Bookstores', fontsize=14)
plt.ylabel('City', fontsize=14)
plt.xticks(rotation=0)

plt.show()