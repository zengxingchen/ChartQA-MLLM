
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 
             2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Books_Published': [250, 275, 300, 325, 400, 500, 600, 700, 800, 900, 1100, 1250, 
                        1400, 1500, 1600, 1700, 1800, 2000, 2100, 2200, 2300, 2400, 
                        2500, 2700]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 9))
plt.fill_between(df['Year'], df['Books_Published'], color='#3498db', alpha=0.6)
plt.plot(df['Year'], df['Books_Published'], color='#e74c3c', alpha=0.8)

plt.title('Number of Books Published Each Year', fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Books Published', fontsize=16)
plt.annotate('Significant Increase in Publishing', xy=(2010, 1100), xytext=(2010, 2000),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=14, color='black')

plt.grid(True)
plt.tight_layout()
plt.show()