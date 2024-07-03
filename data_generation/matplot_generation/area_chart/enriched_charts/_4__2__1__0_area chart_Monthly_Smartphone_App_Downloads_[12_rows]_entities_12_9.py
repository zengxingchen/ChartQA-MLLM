import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
    'Revenue': [110, 145, 210, 280, 270, 300, 320, 340, 370, 395, 420, 450, 475, 495, 520, 540]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
plt.fill_between(df['Year'], df['Revenue'], color='#1f77b4', alpha=0.6)
plt.plot(df['Year'], df['Revenue'], color='#ff7f0e', marker='s')

plt.title('Annual Revenue from Music & Performing Arts (2010-2025)', fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Revenue (in millions)', fontsize=16)

for i, txt in enumerate(df['Revenue']):
    plt.annotate(txt, (df['Year'][i], df['Revenue'][i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)
plt.tight_layout()
plt.show()