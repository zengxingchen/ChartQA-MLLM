
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Month': 'January', 'Running': 10, 'Cycling': 5, 'Swimming': 2},
    {'Month': 'February', 'Running': 12, 'Cycling': 8, 'Swimming': 3},
    {'Month': 'March', 'Running': 8, 'Cycling': 6, 'Swimming': 2},
    {'Month': 'April', 'Running': 15, 'Cycling': 10, 'Swimming': 5},
    {'Month': 'May', 'Running': 20, 'Cycling': 12, 'Swimming': 8},
    {'Month': 'June', 'Running': 18, 'Cycling': 14, 'Swimming': 7},
    {'Month': 'July', 'Running': 22, 'Cycling': 15, 'Swimming': 10},
    {'Month': 'August', 'Running': 25, 'Cycling': 18, 'Swimming': 12},
    {'Month': 'September', 'Running': 30, 'Cycling': 20, 'Swimming': 15},
    {'Month': 'October', 'Running': 28, 'Cycling': 18, 'Swimming': 14},
    {'Month': 'November', 'Running': 25, 'Cycling': 15, 'Swimming': 10},
    {'Month': 'December', 'Running': 22, 'Cycling': 12, 'Swimming': 8}
]

df = pd.DataFrame(data)
df_long = df.melt(id_vars='Month', var_name='Activity', value_name='Count')

pivot_df = df_long.pivot(index='Month', columns='Activity', values='Count')

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
pivot_df.plot(kind='bar', stacked=True, color=colors, figsize=(14, 10), width=0.7)

plt.title('Monthly Physical Activities', pad=20)
plt.xlabel('Month', labelpad=15)
plt.ylabel('Activity Count', labelpad=15)
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()