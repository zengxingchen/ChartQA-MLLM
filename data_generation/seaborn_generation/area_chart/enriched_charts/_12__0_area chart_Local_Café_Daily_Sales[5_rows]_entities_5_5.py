
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Data
data = {
    'Date': pd.date_range(start='2023-03-01', periods=31, freq='D'),
    'Steps': [5000, 6200, 7100, 8000, 8300, 7800, 7500, 8900, 9200, 9400, 9800, 10200, 10500, 11000, 9500, 10000, 
              10300, 10800, 11200, 11500, 11700, 12000, 12500, 12800, 13000, 13200, 13500, 13700, 14000, 14200, 14500]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 8))
sns.set_theme(style="whitegrid")
ax = sns.lineplot(x='Date', y='Steps', data=df, color='#1f77b4')
ax.fill_between(df['Date'], df['Steps'], color="#aec7e8")
ax.set(title='Daily Step Count in March 2023', xlabel='Date', ylabel='Steps')
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

# Annotation
for index, row in df.iterrows():
    ax.text(row['Date'], row['Steps'], f'{row["Steps"]}', 
            ha='center', va='bottom', fontsize=8, color='grey')

plt.show()