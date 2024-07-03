
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    'Fruit_Consumption': [90, 95, 105, 120, 135, 150, 160, 180, 195, 215, 230, 
                          250, 270, 295, 310, 330, 350, 370, 395, 420, 450]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
plt.fill_between(df['Year'], df['Fruit_Consumption'], color='#1f77b4', alpha=0.6)
plt.plot(df['Year'], df['Fruit_Consumption'], color='#ff7f0e', alpha=0.8, linewidth=2)

plt.title('Annual Fruit Consumption (2000-2020)', fontsize=18, pad=30)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Fruit Consumption (kg per capita)', fontsize=14)

for i in range(len(df)):
    plt.text(df['Year'][i], df['Fruit_Consumption'][i] + 5, str(df['Fruit_Consumption'][i]), 
             ha='center', va='bottom', fontsize=10)

plt.grid(True)
plt.show()