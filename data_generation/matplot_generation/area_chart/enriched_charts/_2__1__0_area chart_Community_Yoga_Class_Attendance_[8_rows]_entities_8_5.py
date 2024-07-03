
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 
             2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 
             2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Books_Published': [150, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 275, 
                        290, 310, 330, 350, 370, 390, 410, 430, 450, 470, 490, 510, 
                        530, 550, 570, 590, 610, 630, 650, 670]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 9))
plt.fill_between(df['Year'], df['Books_Published'], color='#4682B4', alpha=0.7)
plt.plot(df['Year'], df['Books_Published'], color='#B22222', alpha=0.9)

plt.title('Number of Books Published Each Year', fontsize=18)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Books Published', fontsize=15)
plt.annotate('Significant increase in publications', xy=(2005, 310), xytext=(2005, 500),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='black')

plt.grid(True)
plt.tight_layout()
plt.show()