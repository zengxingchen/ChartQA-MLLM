
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Year": [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    "Revenue Generated": [50, 52, 54, 60, 65, 70, 75, 85, 90, 100, 110, 120, 130, 
                          145, 160, 175, 190, 210, 230, 250, 270, 300]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
plt.fill_between(df["Year"], df["Revenue Generated"], color="#FF6347", alpha=0.6)

plt.title('Annual Revenue Generated (2000-2021)', fontsize=20, pad=35)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Revenue Generated (in Millions)', fontsize=16)
plt.annotate('Sharp Increase', xy=(2015, 175), xytext=(2012, 200),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=14, color='black')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()