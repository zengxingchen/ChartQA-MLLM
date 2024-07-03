
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Year": [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021,
             2022, 2023, 2024],
    "Revenue (Billion USD)": [120.5, 130.2, 140.1, 145.3, 150.7, 155.6, 160.8, 
                              170.5, 175.9, 180.3, 185.7, 190.2, 195.8, 200.4, 
                              205.7, 210.1, 215.6, 220.9, 225.3, 230.8, 235.2, 
                              240.5, 245.9, 250.4, 255.8]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 9))
plt.fill_between(df["Year"], df["Revenue (Billion USD)"], color="#4682B4", alpha=0.7)

plt.title('Annual Revenue Growth (2000-2024)', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Revenue (Billion USD)', fontsize=15)
plt.annotate('Sharp Increase', xy=(2010, 185.7), xytext=(2005, 200),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=13, color='black')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()