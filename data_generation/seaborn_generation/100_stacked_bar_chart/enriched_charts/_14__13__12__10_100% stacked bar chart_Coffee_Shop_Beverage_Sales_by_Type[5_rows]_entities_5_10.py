
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Date': '2023-01-01', 'Streaming': '20%', 'Books': '25%', 'Games': '30%', 'Movies': '15%', 'Music': '10%'},
    {'Date': '2023-02-01', 'Streaming': '18%', 'Books': '27%', 'Games': '28%', 'Movies': '17%', 'Music': '10%'},
    {'Date': '2023-03-01', 'Streaming': '22%', 'Books': '24%', 'Games': '26%', 'Movies': '18%', 'Music': '10%'},
    {'Date': '2023-04-01', 'Streaming': '19%', 'Books': '26%', 'Games': '25%', 'Movies': '20%', 'Music': '10%'},
    {'Date': '2023-05-01', 'Streaming': '21%', 'Books': '23%', 'Games': '27%', 'Movies': '19%', 'Music': '10%'},
    {'Date': '2023-06-01', 'Streaming': '20%', 'Books': '25%', 'Games': '28%', 'Movies': '17%', 'Music': '10%'},
    {'Date': '2023-07-01', 'Streaming': '18%', 'Books': '26%', 'Games': '29%', 'Movies': '17%', 'Music': '10%'},
    {'Date': '2023-08-01', 'Streaming': '19%', 'Books': '27%', 'Games': '28%', 'Movies': '16%', 'Music': '10%'},
    {'Date': '2023-09-01', 'Streaming': '21%', 'Books': '24%', 'Games': '30%', 'Movies': '15%', 'Music': '10%'},
    {'Date': '2023-10-01', 'Streaming': '20%', 'Books': '25%', 'Games': '27%', 'Movies': '18%', 'Music': '10%'},
]

df = pd.DataFrame(data)

for col in df.columns:
    if col != 'Date':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Date', var_name='Category', value_name='Percentage')

df_long['Date'] = pd.to_datetime(df_long['Date'])
df_long.sort_values(by='Date', inplace=True)

categories = df.columns[1:]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFC300']

left = len(df_long['Date'].unique()) * [0]

fig, ax = plt.subplots(figsize=(14, 8))

for ix, category in enumerate(categories):
    category_data = df_long[df_long['Category'] == category]
    plt.bar(
        category_data['Date'].dt.strftime('%Y-%m-%d'),
        category_data['Percentage'],
        width=0.8,
        bottom=left,
        color=colors[ix],
        edgecolor="white",
        label=category
    )
    left = left + category_data['Percentage'].values

plt.xticks(rotation=45)
plt.yticks(ticks=[0, 0.25, 0.5, 0.75, 1], labels=['0%', '25%', '50%', '75%', '100%'])
plt.ylabel('Percentage')
plt.title('Monthly Entertainment Consumption Distribution (Entertainment & Leisure)', pad=20)
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()

plt.show()