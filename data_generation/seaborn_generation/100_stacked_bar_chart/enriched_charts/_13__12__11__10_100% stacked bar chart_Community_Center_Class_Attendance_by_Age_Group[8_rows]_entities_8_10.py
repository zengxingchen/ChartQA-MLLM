
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Month': 'January', 'Hiking': '20%', 'Cycling': '40%', 'Kayaking': '40%'},
    {'Month': 'February', 'Hiking': '22%', 'Cycling': '38%', 'Kayaking': '40%'},
    {'Month': 'March', 'Hiking': '24%', 'Cycling': '36%', 'Kayaking': '40%'},
    {'Month': 'April', 'Hiking': '26%', 'Cycling': '34%', 'Kayaking': '40%'},
    {'Month': 'May', 'Hiking': '28%', 'Cycling': '32%', 'Kayaking': '40%'},
    {'Month': 'June', 'Hiking': '30%', 'Cycling': '30%', 'Kayaking': '40%'},
    {'Month': 'July', 'Hiking': '32%', 'Cycling': '28%', 'Kayaking': '40%'},
    {'Month': 'August', 'Hiking': '34%', 'Cycling': '26%', 'Kayaking': '40%'},
    {'Month': 'September', 'Hiking': '36%', 'Cycling': '24%', 'Kayaking': '40%'},
    {'Month': 'October', 'Hiking': '38%', 'Cycling': '22%', 'Kayaking': '40%'},
    {'Month': 'November', 'Hiking': '40%', 'Cycling': '20%', 'Kayaking': '40%'},
    {'Month': 'December', 'Hiking': '42%', 'Cycling': '18%', 'Kayaking': '40%'}
]

df = pd.DataFrame(data)
for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Month', var_name='Activity', value_name='Percentage')

pivot_df = df_long.pivot(index='Month', columns='Activity', values='Percentage')

colors = ['#FF6347', '#4682B4', '#32CD32']
pivot_df.plot(kind='bar', stacked=True, color=colors, figsize=(12, 8), width=0.7)

plt.title('Monthly Traveler Activities Participation', pad=20)
plt.xlabel('Month', labelpad=15)
plt.ylabel('Percentage', labelpad=15)
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()