
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Rainfall': [78, 82, 90, 105, 130, 150, 160, 155, 140, 110, 90, 85]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))

ax = sns.lineplot(x='Month', y='Average_Rainfall', data=df, color='#1f77b4')
plt.fill_between(df['Month'], df['Average_Rainfall'], color='#1f77b4', alpha=0.3)

plt.text(6, 160, 'Peak Rainfall', horizontalalignment='left', size='medium', color='black')

plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Average Rainfall (mm)')
plt.title('Monthly Average Rainfall')

plt.tight_layout()
plt.show()