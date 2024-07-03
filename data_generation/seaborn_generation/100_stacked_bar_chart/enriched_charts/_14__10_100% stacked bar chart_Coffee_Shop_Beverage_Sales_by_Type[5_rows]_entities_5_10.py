
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime

data = [
    {'Date': '2023-01-01', 'Reading': '20%', 'Writing': '30%', 'Math': '25%', 'Science': '15%', 'History': '10%'},
    {'Date': '2023-02-01', 'Reading': '25%', 'Writing': '25%', 'Math': '20%', 'Science': '20%', 'History': '10%'},
    {'Date': '2023-03-01', 'Reading': '30%', 'Writing': '20%', 'Math': '25%', 'Science': '15%', 'History': '10%'},
    {'Date': '2023-04-01', 'Reading': '35%', 'Writing': '20%', 'Math': '20%', 'Science': '15%', 'History': '10%'},
    {'Date': '2023-05-01', 'Reading': '30%', 'Writing': '25%', 'Math': '20%', 'Science': '15%', 'History': '10%'},
    {'Date': '2023-06-01', 'Reading': '25%', 'Writing': '30%', 'Math': '25%', 'Science': '10%', 'History': '10%'}
]

df = pd.DataFrame(data)

for col in df.columns:
    if col != 'Date':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Date', var_name='Subject', value_name='Percentage')

df_long['Date'] = pd.to_datetime(df_long['Date'])
df_long.sort_values(by='Date', inplace=True)

subjects = df.columns[1:]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

left = len(df_long['Date'].unique()) * [0]

fig, ax = plt.subplots(figsize=(10, 6))

for ix, subject in enumerate(subjects):
    subject_data = df_long[df_long['Subject'] == subject]
    plt.bar(
        subject_data['Date'].dt.strftime('%Y-%m-%d'),
        subject_data['Percentage'],
        width=0.5,
        bottom=left,
        color=colors[ix],
        edgecolor="white",
        label=subject
    )
    left = left + subject_data['Percentage'].values

plt.xticks(rotation=45)
plt.yticks(ticks=[0, 0.25, 0.5, 0.75, 1], labels=['0%', '25%', '50%', '75%', '100%'])
plt.ylabel('Percentage')
plt.title('Student Performance Distribution Over Time')
plt.legend(title='Subject', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()