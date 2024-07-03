
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2019, 2019, 2019, 2019, 2020, 2020, 2020, 2020, 2021, 2021, 2021, 2021, 2022, 2022, 2022, 2022, 2023, 2023, 2023, 2023],
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4'],
    'GDP Growth (%)': [2.5, 2.3, 2.7, 2.8, -1.5, -9.0, 6.5, 3.0, 1.2, 4.5, 2.9, 3.5, 3.0, 3.2, 3.8, 2.5, 2.7, 2.9, 2.8, 3.1]
}

df = pd.DataFrame(data)
df['Period'] = df['Year'].astype(str) + '-' + df['Quarter']

plt.figure(figsize=(16, 8))
plt.fill_between(df['Period'], df['GDP Growth (%)'], color='#FF6347', alpha=0.7)

for i in range(len(df)):
    plt.text(i, df['GDP Growth (%)'][i], str(df['GDP Growth (%)'][i]), ha='center', va='bottom', fontsize=8)

plt.title('Quarterly GDP Growth (%) Over Five Years', fontsize=18, pad=20, y=1.05)
plt.xlabel('Period', fontsize=14)
plt.ylabel('GDP Growth (%)', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('GDP_Growth_Area_Chart.png')
plt.show()