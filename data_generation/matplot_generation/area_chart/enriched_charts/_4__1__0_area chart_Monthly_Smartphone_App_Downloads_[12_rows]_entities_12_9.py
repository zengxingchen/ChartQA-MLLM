
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035],
    'Calories Burned': [120, 135, 150, 160, 170, 190, 210, 230, 250, 265, 280, 300, 315, 330, 345, 360, 375, 390, 405, 420, 435, 450, 465, 480, 495, 510]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 9))
plt.fill_between(df['Year'], df['Calories Burned'], color='#00bfff', alpha=0.6)
plt.plot(df['Year'], df['Calories Burned'], color='#ff4500', marker='o')

plt.title('Annual Calories Burned from 2010 to 2035', fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Calories Burned (in thousands)', fontsize=14)

for i, txt in enumerate(df['Calories Burned']):
    plt.annotate(txt, (df['Year'][i], df['Calories Burned'][i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)
plt.tight_layout()
plt.show()