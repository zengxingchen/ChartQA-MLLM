
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2018, 'Streaming Services (%)': 30, 'Cable TV (%)': 25, 'Satellite TV (%)': 20, 'DVD/Blu-ray (%)': 15, 'Online Rentals (%)': 10},
    {'Year': 2019, 'Streaming Services (%)': 35, 'Cable TV (%)': 20, 'Satellite TV (%)': 15, 'DVD/Blu-ray (%)': 20, 'Online Rentals (%)': 10},
    {'Year': 2020, 'Streaming Services (%)': 40, 'Cable TV (%)': 15, 'Satellite TV (%)': 10, 'DVD/Blu-ray (%)': 25, 'Online Rentals (%)': 10},
    {'Year': 2021, 'Streaming Services (%)': 45, 'Cable TV (%)': 15, 'Satellite TV (%)': 10, 'DVD/Blu-ray (%)': 20, 'Online Rentals (%)': 10},
    {'Year': 2022, 'Streaming Services (%)': 50, 'Cable TV (%)': 10, 'Satellite TV (%)': 10, 'DVD/Blu-ray (%)': 20, 'Online Rentals (%)': 10},
    {'Year': 2023, 'Streaming Services (%)': 55, 'Cable TV (%)': 10, 'Satellite TV (%)': 10, 'DVD/Blu-ray (%)': 15, 'Online Rentals (%)': 10},
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
cumulative_values = df.cumsum(axis=1)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.7
for i, col in enumerate(df.columns):
    bottom_values = cumulative_values.iloc[:, i-1] if i > 0 else None
    ax.bar(df.index, df[col], bottom=bottom_values, color=colors[i], edgecolor='white', label=col, width=bar_width)

ax.set_xticks(df.index)
ax.set_xticklabels(df.index, rotation=0)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Distribution of TV and Video Viewing Methods Over Years', pad=20)
ax.legend(title='Viewing Method', bbox_to_anchor=(1.05, 1), loc='upper left')

yticks = ax.get_yticks()
ax.set_yticklabels(['{}%'.format(int(y)) for y in yticks])

plt.tight_layout()
plt.show()