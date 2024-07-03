
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December'],
    'Number_of_Tourists': [500, 800, 700, 1000, 1200, 1500, 1800, 1700, 1600, 1400, 1100, 900]
}

df = pd.DataFrame(data)

month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

plt.figure(figsize=(14, 7))

lineplot = sns.lineplot(x='Month', y='Number_of_Tourists', data=df, color="#2ecc71", marker='o')

for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Number_of_Tourists'][i] + 30, f"{df['Number_of_Tourists'][i]}", 
             ha='center', va='bottom', fontsize=9, color='#333333')

plt.title('Monthly Tourist Visits to City (in hundreds)', fontsize=16, loc='left')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Tourists (in hundreds)', fontsize=12)

plt.show()