
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Temperature': [30, 32, 35, 40, 45, 50, 55, 53, 48, 42, 38, 34]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))

ax = sns.lineplot(x='Month', y='Average_Temperature', data=df, color='#e377c2')
plt.fill_between(df['Month'], df['Average_Temperature'], color='#e377c2', alpha=0.3)

plt.text(6, 55, 'Peak Temperature', horizontalalignment='left', size='medium', color='black')

plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.title('Monthly Average Temperature')

plt.tight_layout()
plt.show()