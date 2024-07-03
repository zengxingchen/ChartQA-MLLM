
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Month': 'January', 'Food & Beverage': '15%', 'Electronics': '55%', 'Fashion': '30%'},
    {'Month': 'February', 'Food & Beverage': '20%', 'Electronics': '50%', 'Fashion': '30%'},
    {'Month': 'March', 'Food & Beverage': '25%', 'Electronics': '45%', 'Fashion': '30%'},
    {'Month': 'April', 'Food & Beverage': '22%', 'Electronics': '40%', 'Fashion': '38%'},
    {'Month': 'May', 'Food & Beverage': '30%', 'Electronics': '35%', 'Fashion': '35%'},
    {'Month': 'June', 'Food & Beverage': '28%', 'Electronics': '37%', 'Fashion': '35%'},
    {'Month': 'July', 'Food & Beverage': '25%', 'Electronics': '40%', 'Fashion': '35%'},
    {'Month': 'August', 'Food & Beverage': '27%', 'Electronics': '43%', 'Fashion': '30%'}
]

df = pd.DataFrame(data)
for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Month', var_name='Category', value_name='Percentage')

pivot_df = df_long.pivot(index='Month', columns='Category', values='Percentage')

colors = ['#FF6347', '#4682B4', '#32CD32']
pivot_df.plot(kind='bar', stacked=True, color=colors, figsize=(14, 8), width=0.8)

plt.title('Monthly Distribution of Sales by Category', pad=20)
plt.xlabel('Month', labelpad=15)
plt.ylabel('Percentage', labelpad=15)
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()