
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Running_Distance': [50, 53, 67, 72, 78, 83, 91, 96, 88, 73, 62, 54]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))

ax = sns.lineplot(x='Month', y='Average_Running_Distance', data=df, color='#1f77b4')
plt.fill_between(df['Month'], df['Average_Running_Distance'], color='#1f77b4', alpha=0.4)

plt.text(7, 96, 'Peak in August', horizontalalignment='left', size='medium', color='black')

plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Average Running Distance (km)')
plt.title('Monthly Average Running Distance - Sports & Fitness', pad=20)

plt.tight_layout()
plt.show()