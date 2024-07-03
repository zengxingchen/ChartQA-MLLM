
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Month': 'January', 'Local Business': '30%', 'Online Shopping': '50%', 'Freelancing': '20%'},
    {'Month': 'February', 'Local Business': '35%', 'Online Shopping': '45%', 'Freelancing': '20%'},
    {'Month': 'March', 'Local Business': '32%', 'Online Shopping': '48%', 'Freelancing': '20%'},
    {'Month': 'April', 'Local Business': '30%', 'Online Shopping': '50%', 'Freelancing': '20%'},
    {'Month': 'May', 'Local Business': '28%', 'Online Shopping': '52%', 'Freelancing': '20%'},
    {'Month': 'June', 'Local Business': '26%', 'Online Shopping': '54%', 'Freelancing': '20%'},
    {'Month': 'July', 'Local Business': '24%', 'Online Shopping': '56%', 'Freelancing': '20%'},
    {'Month': 'August', 'Local Business': '22%', 'Online Shopping': '58%', 'Freelancing': '20%'},
    {'Month': 'September', 'Local Business': '20%', 'Online Shopping': '60%', 'Freelancing': '20%'},
    {'Month': 'October', 'Local Business': '18%', 'Online Shopping': '62%', 'Freelancing': '20%'},
    {'Month': 'November', 'Local Business': '16%', 'Online Shopping': '64%', 'Freelancing': '20%'},
    {'Month': 'December', 'Local Business': '14%', 'Online Shopping': '66%', 'Freelancing': '20%'}
]

df = pd.DataFrame(data)
for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Month', var_name='Activity', value_name='Percentage')

pivot_df = df_long.pivot(index='Month', columns='Activity', values='Percentage')

colors = ['#FF4500', '#1E90FF', '#32CD32']
pivot_df.plot(kind='bar', stacked=True, color=colors, figsize=(10, 6), width=0.5)

plt.title('Monthly Participation in Business Activities', pad=20)
plt.xlabel('Month', labelpad=15)
plt.ylabel('Percentage', labelpad=15)
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()