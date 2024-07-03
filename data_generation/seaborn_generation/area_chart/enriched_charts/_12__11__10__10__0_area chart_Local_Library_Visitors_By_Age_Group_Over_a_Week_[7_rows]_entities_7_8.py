import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [100, 120, 150, 170, 220, 250, 270, 260, 230, 200, 180, 140]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))

ax = sns.lineplot(x='Month', y='Revenue', data=df, color='#FF4500')
plt.fill_between(df['Month'], df['Revenue'], color='#FFD700', alpha=0.6)

plt.text(6, 280, 'Peak Monthly Revenue', horizontalalignment='left', size='medium', color='black')

plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Revenue in Thousands')
plt.title('Monthly Revenue for a Retail Store')

plt.tight_layout()
plt.show()