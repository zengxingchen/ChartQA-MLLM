
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
    'Viewership': [85, 105, 115, 130, 150, 165, 175, 180, 190, 200, 220, 240, 260, 280, 300, 310]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
plt.fill_between(df['Year'], df['Viewership'], color='#ff6347', alpha=0.7)
plt.plot(df['Year'], df['Viewership'], color='#4682b4', marker='o')

plt.title('Annual TV Show Viewership from 2010 to 2025', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Viewership (in millions)', fontsize=16)

for i, txt in enumerate(df['Viewership']):
    plt.annotate(txt, (df['Year'][i], df['Viewership'][i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)
plt.tight_layout()
plt.show()