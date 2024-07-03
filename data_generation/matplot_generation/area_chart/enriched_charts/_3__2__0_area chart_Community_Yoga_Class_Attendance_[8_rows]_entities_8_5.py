
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [
        '2015-Q1', '2015-Q2', '2015-Q3', '2015-Q4', '2016-Q1', '2016-Q2', 
        '2016-Q3', '2016-Q4', '2017-Q1', '2017-Q2', '2017-Q3', '2017-Q4', 
        '2018-Q1', '2018-Q2', '2018-Q3', '2018-Q4', '2019-Q1', '2019-Q2', 
        '2019-Q3', '2019-Q4', '2020-Q1', '2020-Q2', '2020-Q3', '2020-Q4', 
        '2021-Q1', '2021-Q2', '2021-Q3', '2021-Q4', '2022-Q1', '2022-Q2', 
        '2022-Q3', '2022-Q4', '2023-Q1', '2023-Q2', '2023-Q3', '2023-Q4', 
        '2024-Q1', '2024-Q2', '2024-Q3', '2024-Q4'
    ],
    'GDP_Growth': [
        2.5, 2.7, 2.6, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 
        3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.0, 3.8, 4.2, 4.4, 
        4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 
        5.7, 5.8, 5.9, 6.0
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
plt.style.use('seaborn-whitegrid')

color = "#3498db"

area_plot = plt.plot(df['Year'], df['GDP_Growth'], color=color)
plt.fill_between(df['Year'], df['GDP_Growth'], alpha=0.3, color=color)

for index, row in df.iterrows():
    plt.text(index, row['GDP_Growth'] + 0.1, round(row['GDP_Growth'], 2), 
             color='black', ha="center", fontsize=8)

plt.title('Quarterly GDP Growth Rate of Country X (2015-2024)', fontsize=18, pad=20)
plt.xlabel('Year-Quarter')
plt.ylabel('GDP Growth Rate (%)')

plt.show()