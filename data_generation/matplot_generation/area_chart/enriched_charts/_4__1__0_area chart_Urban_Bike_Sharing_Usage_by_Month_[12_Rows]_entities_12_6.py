
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2019, 2019, 2019, 2019, 2020, 2020, 2020, 2020, 2021, 2021, 2021, 2021, 2022, 2022, 2022, 2022, 2023, 2023, 2023, 2023],
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4'],
    'Art Sales (in millions)': [45.0, 47.5, 50.0, 52.5, 30.0, 20.0, 35.0, 40.0, 55.0, 60.0, 62.0, 65.0, 70.0, 72.5, 75.0, 77.5, 80.0, 82.5, 85.0, 87.5]
}

df = pd.DataFrame(data)
df['Period'] = df['Year'].astype(str) + '-' + df['Quarter']

plt.figure(figsize=(14, 7))
plt.fill_between(df['Period'], df['Art Sales (in millions)'], color='#1E90FF', alpha=0.6)

for i in range(len(df)):
    plt.text(i, df['Art Sales (in millions)'][i], str(df['Art Sales (in millions)'][i]), ha='center', va='bottom')

plt.title('Quarterly Art Sales (in millions) Over Five Years', fontsize=16, pad=20)
plt.xlabel('Period', fontsize=12)
plt.ylabel('Art Sales (in millions)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('Art_Sales_Area_Chart.png')
plt.show()