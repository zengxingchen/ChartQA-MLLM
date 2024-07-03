
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Destination': 'Europe', 'Sightseeing': '30%', 'Adventure Activities': '15%', 'Cultural Tours': '20%', 'Relaxation': '25%', 'Wildlife Safari': '5%', 'Culinary Experiences': '5%'},
    {'Destination': 'Asia', 'Sightseeing': '20%', 'Adventure Activities': '30%', 'Cultural Tours': '15%', 'Relaxation': '10%', 'Wildlife Safari': '15%', 'Culinary Experiences': '10%'},
    {'Destination': 'Africa', 'Sightseeing': '10%', 'Adventure Activities': '35%', 'Cultural Tours': '10%', 'Relaxation': '15%', 'Wildlife Safari': '20%', 'Culinary Experiences': '10%'},
    {'Destination': 'North America', 'Sightseeing': '25%', 'Adventure Activities': '20%', 'Cultural Tours': '20%', 'Relaxation': '10%', 'Wildlife Safari': '15%', 'Culinary Experiences': '10%'},
    {'Destination': 'South America', 'Sightseeing': '15%', 'Adventure Activities': '25%', 'Cultural Tours': '15%', 'Relaxation': '20%', 'Wildlife Safari': '15%', 'Culinary Experiences': '10%'},
    {'Destination': 'Australia', 'Sightseeing': '20%', 'Adventure Activities': '20%', 'Cultural Tours': '15%', 'Relaxation': '20%', 'Wildlife Safari': '15%', 'Culinary Experiences': '10%'},
    {'Destination': 'Antarctica', 'Sightseeing': '5%', 'Adventure Activities': '10%', 'Cultural Tours': '5%', 'Relaxation': '10%', 'Wildlife Safari': '35%', 'Culinary Experiences': '35%'}
]

df = pd.DataFrame(data)
df = df.set_index('Destination')
df = df.applymap(lambda x: int(x.replace('%', '')))

cumulative_sum = df.cumsum(axis=1)

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#ADFF2F']

fig, ax = plt.subplots(figsize=(12, 8))

bottom = None

for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color)
    bottom = cumulative_sum[column]

ax.legend(title='Travel Activities', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_ylabel('Percentage')
ax.set_xlabel('Destination')
ax.set_title('Popular Travel Activities by Destination')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()