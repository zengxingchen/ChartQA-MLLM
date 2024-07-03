
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    'Visitors': [120, 135, 150, 175, 190, 205, 220, 245, 270, 295, 320, 345, 370, 
                 395, 420, 445, 470, 495, 520, 545, 570]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))
plt.fill_between(df['Year'], df['Visitors'], color='#2ca02c', alpha=0.7)
plt.plot(df['Year'], df['Visitors'], color='#d62728', alpha=0.7)

plt.title('Historical Museum Visitors (2000-2020)', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Number of Visitors (in thousands)')

for i in range(len(df)):
    plt.text(df['Year'][i], df['Visitors'][i] + 5, str(df['Visitors'][i]), ha='center', va='bottom', fontsize=9)

plt.grid(True)
plt.show()