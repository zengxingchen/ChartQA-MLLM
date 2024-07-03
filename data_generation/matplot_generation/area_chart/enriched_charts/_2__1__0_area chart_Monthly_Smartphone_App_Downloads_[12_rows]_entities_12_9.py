
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
    'Visitors': [100, 150, 200, 250, 210, 260, 300, 320, 330, 350, 380, 400, 420, 450, 470, 490]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 9))
plt.fill_between(df['Year'], df['Visitors'], color='#2ca02c', alpha=0.7)
plt.plot(df['Year'], df['Visitors'], color='#d62728', marker='o')

plt.title('Annual Visitors to National Parks (2010-2025)', fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Visitors (in thousands)', fontsize=14)

for i, txt in enumerate(df['Visitors']):
    plt.annotate(txt, (df['Year'][i], df['Visitors'][i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)
plt.tight_layout()
plt.show()