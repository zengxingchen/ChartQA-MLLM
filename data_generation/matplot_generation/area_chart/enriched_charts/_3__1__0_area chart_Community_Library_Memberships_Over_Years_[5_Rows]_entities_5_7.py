
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    'Vegetable_Consumption': [100, 110, 125, 140, 155, 170, 185, 205, 225, 245, 270, 
                              295, 315, 340, 360, 380, 400, 420, 445, 470, 500]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
plt.fill_between(df['Year'], df['Vegetable_Consumption'], color='#2ca02c', alpha=0.6)
plt.plot(df['Year'], df['Vegetable_Consumption'], color='#d62728', alpha=0.8, linewidth=2)

plt.title('Annual Vegetable Consumption (2000-2020)', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Vegetable Consumption (kg per capita)', fontsize=12)

for i in range(len(df)):
    plt.text(df['Year'][i], df['Vegetable_Consumption'][i] + 5, str(df['Vegetable_Consumption'][i]), 
             ha='center', va='bottom', fontsize=9)

plt.grid(True)
plt.show()