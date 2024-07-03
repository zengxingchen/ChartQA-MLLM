
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    'Sales': [150, 165, 180, 190, 210, 230, 250, 275, 300, 330, 360, 390, 420, 
              450, 480, 510, 540, 580, 620, 660, 700]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))
plt.fill_between(df['Year'], df['Sales'], color='#1f77b4', alpha=0.7)
plt.plot(df['Year'], df['Sales'], color='#ff7f0e', alpha=0.7)

plt.title('Annual Sales Growth (2000-2020)')
plt.xlabel('Year')
plt.ylabel('Sales ($ in millions)')

for i in range(len(df)):
    plt.text(df['Year'][i], df['Sales'][i] + 10, str(df['Sales'][i]), ha='center', va='bottom')

plt.grid(True)
plt.show()