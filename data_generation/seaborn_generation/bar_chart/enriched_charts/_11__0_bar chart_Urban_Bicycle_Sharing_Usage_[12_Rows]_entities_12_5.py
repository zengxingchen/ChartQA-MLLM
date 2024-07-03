
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': ['2023-04-01', '2023-04-02', '2023-04-03', '2023-04-04', 
             '2023-04-05', '2023-04-06', '2023-04-07', '2023-04-08', 
             '2023-04-09', '2023-04-10', '2023-04-11', '2023-04-12', 
             '2023-04-13', '2023-04-14'],
    'Daily Sales': [150, 175, 160, 180, 190, 200, 220, 210, 230, 240, 250, 260, 270, 280]
}

df = pd.DataFrame(data)

# Visualization
plt.figure(figsize=(12, 6))
sns.barplot(x='Date', y='Daily Sales', data=df,
            palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                     '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                     '#bcbd22', '#17becf', '#ff9896', '#c5b0d5',
                     '#c49c94', '#f7b6d2'],
            dodge=False)

plt.xlabel('Date')
plt.ylabel('Daily Sales (in $)')
plt.title('Two-week Daily Sales in Fictitious Store')
sns.despine(left=True, bottom=True)

plt.show()