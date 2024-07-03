
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Data
data = {
    'Date': pd.date_range(start='2023-03-01', periods=31, freq='D'),
    'Steps': [5000, 5200, 4800, 5500, 5700, 5900, 6100, 6300, 6000, 6500, 6700, 6900, 7100, 7300, 7500,
              7700, 7900, 8100, 8300, 8500, 8700, 8900, 9100, 9300, 9500, 9700, 9900, 10100, 10300, 10500, 10700]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 8))
sns.set_theme(style="whitegrid")
ax = sns.lineplot(x='Date', y='Steps', data=df, color='#FF5733')
ax.fill_between(df['Date'], df['Steps'], color="#FFC300")
ax.set(title='Daily Steps in March 2023', xlabel='Date', ylabel='Steps')
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

# Annotation
for index, row in df.iterrows():
    ax.text(row['Date'], row['Steps'], f'{row["Steps"]}', 
            ha='center', va='bottom', fontsize=8, color='black')

plt.show()