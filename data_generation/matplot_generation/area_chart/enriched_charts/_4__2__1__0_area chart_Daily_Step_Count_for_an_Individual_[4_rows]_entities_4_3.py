import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Year": [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    "Number of Electric Vehicles (Million)": [0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 
                                              2.8, 3.5, 4.2, 5.0, 6.5, 8.0, 10.0, 
                                              12.5, 15.0, 18.0, 21.5, 25.0, 30.0, 35.0, 40.0]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
plt.fill_between(df["Year"], df["Number of Electric Vehicles (Million)"], color="#FF6347", alpha=0.7)

plt.title('Rise of Electric Vehicles (2000-2021)', fontsize=20, pad=30)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Electric Vehicles (Million)', fontsize=14)
plt.annotate('Rapid Growth', xy=(2015, 15.0), xytext=(2010, 10.0),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='black')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()