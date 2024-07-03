
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
    'Visitors': [110, 160, 220, 230, 250, 270, 310, 340, 360, 370, 390, 420, 450, 480, 500, 530]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
plt.fill_between(df['Year'], df['Visitors'], color='#1f77b4', alpha=0.7)
plt.plot(df['Year'], df['Visitors'], color='#ff7f0e', marker='o')

plt.title('Annual Visitors to Art Galleries (2010-2025)', fontsize=20, pad=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Visitors (in thousands)', fontsize=16)

for i, txt in enumerate(df['Visitors']):
    plt.annotate(txt, (df['Year'][i], df['Visitors'][i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)
plt.tight_layout()
plt.show()