
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': ['2023-04-01', '2023-04-02', '2023-04-03', '2023-04-04', 
             '2023-04-05', '2023-04-06', '2023-04-07', '2023-04-08', 
             '2023-04-09', '2023-04-10', '2023-04-11', '2023-04-12', 
             '2023-04-13', '2023-04-14', '2023-04-15', '2023-04-16'],
    'Daily Sales': [150, 175, 160, 180, 190, 200, 220, 210, 230, 240, 250, 260, 270, 280, 290, 300]
}

df = pd.DataFrame(data)

# Visualization
plt.figure(figsize=(10, 8))
sns.barplot(y='Date', x='Daily Sales', data=df,
            palette=['#4daf4a', '#377eb8', '#ff7f00', '#e41a1c',
                     '#984ea3', '#f781bf', '#a65628', '#999999',
                     '#dede00', '#a6cee3', '#1f78b4', '#b2df8a',
                     '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f'],
            linewidth=1.5)

plt.xlabel('Daily Sales (in $)')
plt.ylabel('Date')
plt.title('Two-week Daily Sales in Future Technologies Store', pad=20)
sns.despine(left=True, bottom=True)

plt.show()