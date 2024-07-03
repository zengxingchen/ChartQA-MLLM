
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Category': '2025', 'Artificial Intelligence': '20%', 'Renewable Energy': '15%', 'Quantum Computing': '25%', 'Space Exploration': '10%', 'Biotechnology': '20%', 'Cybersecurity': '10%'},
    {'Category': '2030', 'Artificial Intelligence': '25%', 'Renewable Energy': '20%', 'Quantum Computing': '15%', 'Space Exploration': '15%', 'Biotechnology': '15%', 'Cybersecurity': '10%'},
    {'Category': '2035', 'Artificial Intelligence': '30%', 'Renewable Energy': '25%', 'Quantum Computing': '20%', 'Space Exploration': '10%', 'Biotechnology': '10%', 'Cybersecurity': '5%'},
    {'Category': '2040', 'Artificial Intelligence': '15%', 'Renewable Energy': '30%', 'Quantum Computing': '15%', 'Space Exploration': '20%', 'Biotechnology': '10%', 'Cybersecurity': '10%'},
    {'Category': '2045', 'Artificial Intelligence': '20%', 'Renewable Energy': '20%', 'Quantum Computing': '10%', 'Space Exploration': '30%', 'Biotechnology': '10%', 'Cybersecurity': '10%'},
    {'Category': '2050', 'Artificial Intelligence': '15%', 'Renewable Energy': '25%', 'Quantum Computing': '20%', 'Space Exploration': '20%', 'Biotechnology': '10%', 'Cybersecurity': '10%'},
    {'Category': '2055', 'Artificial Intelligence': '10%', 'Renewable Energy': '15%', 'Quantum Computing': '25%', 'Space Exploration': '30%', 'Biotechnology': '10%', 'Cybersecurity': '10%'}
]

df = pd.DataFrame(data)
df = df.set_index('Category')
df = df.applymap(lambda x: int(x.replace('%', '')))

cumulative_sum = df.cumsum(axis=1)

colors = ['#FF5733', '#33FF57', '#3357FF', '#F1C40F', '#8E44AD', '#1ABC9C']

fig, ax = plt.subplots(figsize=(10, 14))

bottom = None

for column, color in zip(df.columns, colors):
    ax.barh(df.index, df[column], left=bottom, label=column, color=color, height=0.5)
    bottom = cumulative_sum[column]

ax.legend(title='Tech Investments', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_xlabel('Percentage')
ax.set_ylabel('Year')
ax.set_title('Projected Investments in Future Technologies Over Time', pad=20)

plt.tight_layout()
plt.show()