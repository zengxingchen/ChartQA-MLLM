
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Hours': [10, 12, 15, 18, 22, 25, 28, 26, 24, 20, 16, 12]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))

ax = sns.lineplot(x='Month', y='Hours', data=df, color='#4B0082')
plt.fill_between(df['Month'], df['Hours'], color='#9370DB', alpha=0.6)

plt.text(6, 30, 'Peak Meditation Hours', horizontalalignment='left', size='medium', color='black')

plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Hours of Meditation')
plt.title('Monthly Meditation Hours Logged by Individual')

plt.tight_layout()
plt.show()