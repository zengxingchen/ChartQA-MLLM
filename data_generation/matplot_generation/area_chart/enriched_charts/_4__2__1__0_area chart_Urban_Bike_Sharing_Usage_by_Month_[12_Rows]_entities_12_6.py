
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2019, 2019, 2019, 2019, 2020, 2020, 2020, 2020, 2021, 2021, 2021, 2021, 2022, 2022, 2022, 2022, 2023, 2023, 2023, 2023],
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4'],
    'Internet Users (Millions)': [3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400]
}

df = pd.DataFrame(data)
df['Period'] = df['Year'].astype(str) + '-' + df['Quarter']

plt.figure(figsize=(16, 8))
plt.fill_between(df['Period'], df['Internet Users (Millions)'], color='#FF6347', alpha=0.7)

for i in range(len(df)):
    plt.text(i, df['Internet Users (Millions)'][i], str(df['Internet Users (Millions)'][i]), ha='center', va='bottom', fontsize=8)

plt.title('Quarterly Internet Users Growth (Millions) Over Five Years', fontsize=18, pad=20)
plt.xlabel('Period', fontsize=14)
plt.ylabel('Internet Users (Millions)', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('Internet_Users_Area_Chart.png')
plt.show()