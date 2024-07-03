
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Data
data = {
    'Date': pd.date_range(start='2023-03-01', periods=31, freq='D'),
    'Revenue': [100, 105, 98, 120, 130, 125, 115, 110, 135, 140, 150, 145, 155, 160, 158,
                165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 7))
sns.set_theme(style="whitegrid")
ax = sns.lineplot(x='Date', y='Revenue', data=df, color='#1f77b4')
ax.fill_between(df['Date'], df['Revenue'], color="#aec7e8")
ax.set(title='Daily Revenue in March 2023', xlabel='Date', ylabel='Revenue ($)')
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

# Annotation
for index, row in df.iterrows():
    ax.text(row['Date'], row['Revenue'], f'${row["Revenue"]}', 
            ha='center', va='bottom', fontsize=8, color='black')

plt.show()