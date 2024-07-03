
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': ['2023-04-01', '2023-04-02', '2023-04-03', '2023-04-04', 
             '2023-04-05', '2023-04-06', '2023-04-07', '2023-04-08', 
             '2023-04-09', '2023-04-10', '2023-04-11', '2023-04-12', 
             '2023-04-13', '2023-04-14'],
    'Number of Tickets Sold': [120, 140, 130, 155, 145, 165, 175, 185, 170, 160, 180, 175, 190, 200]
}

df = pd.DataFrame(data)

# Visualization
plt.figure(figsize=(10, 8))
sns.barplot(x='Number of Tickets Sold', y='Date', data=df,
            palette=['#4daf4a', '#377eb8', '#ff7f00', '#984ea3',
                     '#e41a1c', '#a65628', '#f781bf', '#999999',
                     '#dede00', '#f0e442', '#b3de69', '#bc80bd',
                     '#ccebc5', '#ffed6f'],
            width=0.7,
            orient='h')

plt.xlabel('Number of Tickets Sold')
plt.ylabel('Date')
plt.title('Daily Ticket Sales for a Concert Series', pad=20)
sns.despine(left=True, bottom=True)

plt.show()