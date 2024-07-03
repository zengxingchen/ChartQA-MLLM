
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': ['2023-04-01', '2023-04-02', '2023-04-03', '2023-04-04', 
             '2023-04-05', '2023-04-06', '2023-04-07', '2023-04-08', 
             '2023-04-09', '2023-04-10', '2023-04-11', '2023-04-12', 
             '2023-04-13', '2023-04-14'],
    'Number of Tourists': [120, 130, 145, 160, 155, 170, 180, 190, 175, 160, 150, 165, 185, 200]
}

df = pd.DataFrame(data)

# Visualization
plt.figure(figsize=(12, 6))
sns.barplot(x='Date', y='Number of Tourists', data=df,
            palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                     '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                     '#bcbd22', '#17becf', '#aec7e8', '#ffbb78',
                     '#98df8a', '#ff9896'],
            width=0.6,
            orient='v')

plt.xlabel('Date')
plt.ylabel('Number of Tourists')
plt.title('Two-week Tourist Visits in Fictitious City', pad=20)
sns.despine(left=True, bottom=True)

plt.show()