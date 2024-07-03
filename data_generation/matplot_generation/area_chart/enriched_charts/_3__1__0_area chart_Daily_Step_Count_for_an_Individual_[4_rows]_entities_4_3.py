
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Year": [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    "Articles Published": [100, 105, 110, 120, 130, 135, 140, 145, 155, 160, 
                           170, 175, 180, 190, 200, 210, 220, 225, 230, 240, 
                           250, 260]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
plt.fill_between(df["Year"], df["Articles Published"], color="#4682B4", alpha=0.7)

plt.title('Annual Research Articles Published (2000-2021)', fontsize=18, pad=30)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Articles Published', fontsize=14)
plt.annotate('Significant Growth', xy=(2015, 210), xytext=(2010, 230),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='black')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()