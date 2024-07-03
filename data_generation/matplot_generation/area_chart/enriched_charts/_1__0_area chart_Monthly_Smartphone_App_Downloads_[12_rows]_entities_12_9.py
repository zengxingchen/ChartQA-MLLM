
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    'Sales': [150, 200, 250, 180, 300, 270, 320, 310, 330, 290, 340, 360, 370]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
plt.fill_between(df['Year'], df['Sales'], color='#1f77b4', alpha=0.7)
plt.plot(df['Year'], df['Sales'], color='#ff7f0e', marker='o')

plt.title('Annual Sales from 2010 to 2022', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Sales (in thousands)', fontsize=14)

for i, txt in enumerate(df['Sales']):
    plt.annotate(txt, (df['Year'][i], df['Sales'][i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)
plt.tight_layout()
plt.show()