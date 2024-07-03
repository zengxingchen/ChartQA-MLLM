
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Book_Club_Attendance': [8, 12, 18, 22, 26, 30, 34, 32, 28, 24, 20, 14]
}
df = pd.DataFrame(data)

df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

sns.set_theme()

plt.figure(figsize=(14, 7))
area_chart = sns.lineplot(data=df, x='Month', y='Book_Club_Attendance', sort=False, color='#2ca02c')
area_chart.fill_between(df['Month'], df['Book_Club_Attendance'], alpha=0.4, color='#2ca02c')

plt.text(x='July', y=34, s='Peak Attendance (34)', color='red', va='bottom', ha='center')

plt.title('Monthly Book Club Attendance')
plt.xlabel('Month')
plt.ylabel('Attendance')

plt.tight_layout()
plt.show()