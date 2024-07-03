
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2019, 2019, 2019, 2019, 2020, 2020, 2020, 2020, 2021, 2021, 2021, 2021, 2022, 2022, 2022, 2022, 2023, 2023, 2023, 2023],
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4'],
    'Temperature (°C)': [15.0, 16.5, 18.0, 14.0, 13.5, 17.0, 19.5, 14.5, 15.5, 18.0, 20.0, 16.0, 14.0, 16.5, 17.5, 13.5, 14.5, 17.0, 18.5, 15.0]
}

df = pd.DataFrame(data)
df['Period'] = df['Year'].astype(str) + '-' + df['Quarter']

plt.figure(figsize=(14, 8))
plt.fill_between(df['Period'], df['Temperature (°C)'], color='#4682B4', alpha=0.7)

for i in range(len(df)):
    plt.text(i, df['Temperature (°C)'][i], str(df['Temperature (°C)'][i]), ha='center', va='bottom')

plt.title('Quarterly Average Temperature (°C) Over Five Years', fontsize=18, pad=30)
plt.xlabel('Period', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('Temperature_Area_Chart.png')
plt.show()