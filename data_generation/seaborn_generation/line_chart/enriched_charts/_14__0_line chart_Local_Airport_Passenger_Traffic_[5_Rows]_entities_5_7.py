
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December'],
    'Visits': [150, 200, 250, 220, 300, 350, 380, 370, 340, 290, 260, 310]
}

df = pd.DataFrame(data)

month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

plt.figure(figsize=(14, 8))

lineplot = sns.lineplot(x='Month', y='Visits', data=df, color="#e74c3c", marker='o')

for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Visits'][i] + 5, f"{df['Visits'][i]}", 
             ha='center', va='bottom', fontsize=9, color='#2c3e50')

plt.title('Monthly Tourist Visits to National Park', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Visits', fontsize=14)

plt.show()