
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Data
data = {
    'Date': pd.date_range(start='2023-03-01', periods=31, freq='D'),
    'Temperature': [47, 49, 53, 54, 58, 60, 59, 55, 53, 50, 49, 52, 58, 62, 65,
                    60, 58, 57, 56, 59, 63, 61, 64, 66, 67, 68, 70, 74, 75, 77, 76]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")
ax = sns.lineplot(x='Date', y='Temperature', data=df, color='#FF5733')
ax.fill_between(df['Date'], df['Temperature'], color="#FFC300")
ax.set(title='Daily Temperatures in March 2023', xlabel='Date', ylabel='Temperature (°F)')
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

# Annotation
for index, row in df.iterrows():
    ax.text(row['Date'], row['Temperature'], f'{row["Temperature"]}°F', 
            ha='center', va='bottom', fontsize=8, color='grey')

plt.show()