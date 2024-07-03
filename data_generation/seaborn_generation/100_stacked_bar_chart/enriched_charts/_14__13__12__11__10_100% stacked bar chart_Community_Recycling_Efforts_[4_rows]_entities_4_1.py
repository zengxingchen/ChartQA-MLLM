
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2018, 'Software Development (%)': 15, 'Data Analysis (%)': 20, 'Machine Learning (%)': 25, 'Networking (%)': 20, 'Cybersecurity (%)': 20},
    {'Year': 2019, 'Software Development (%)': 20, 'Data Analysis (%)': 25, 'Machine Learning (%)': 20, 'Networking (%)': 15, 'Cybersecurity (%)': 20},
    {'Year': 2020, 'Software Development (%)': 25, 'Data Analysis (%)': 20, 'Machine Learning (%)': 30, 'Networking (%)': 10, 'Cybersecurity (%)': 15},
    {'Year': 2021, 'Software Development (%)': 30, 'Data Analysis (%)': 15, 'Machine Learning (%)': 25, 'Networking (%)': 15, 'Cybersecurity (%)': 15},
    {'Year': 2022, 'Software Development (%)': 35, 'Data Analysis (%)': 10, 'Machine Learning (%)': 20, 'Networking (%)': 15, 'Cybersecurity (%)': 20},
    {'Year': 2023, 'Software Development (%)': 40, 'Data Analysis (%)': 15, 'Machine Learning (%)': 15, 'Networking (%)': 20, 'Cybersecurity (%)': 10},
    {'Year': 2024, 'Software Development (%)': 45, 'Data Analysis (%)': 10, 'Machine Learning (%)': 10, 'Networking (%)': 25, 'Cybersecurity (%)': 10}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
cumulative_values = df.cumsum(axis=1)

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2']
fig, ax = plt.subplots(figsize=(8, 12))

bar_width = 0.4
for i, col in enumerate(df.columns):
    bottom_values = cumulative_values.iloc[:, i-1] if i > 0 else None
    ax.bar(
        df.index,
        df[col],
        bottom=bottom_values,
        color=colors[i],
        edgecolor='white',
        label=col,
        width=bar_width
    )

ax.set_xticks(df.index)
ax.set_xticklabels(df.index)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Time Spent on IT Skills Development Over Years', pad=20)
ax.legend(title='IT Skill', bbox_to_anchor=(1.05, 1), loc='upper left')

yticks = ax.get_yticks()
ax.set_yticklabels(['{}%'.format(int(y)) for y in yticks])

plt.tight_layout()
plt.show()