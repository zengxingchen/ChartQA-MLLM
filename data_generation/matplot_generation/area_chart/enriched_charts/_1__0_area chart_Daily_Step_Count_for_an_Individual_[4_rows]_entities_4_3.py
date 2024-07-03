
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Year": [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    "CO2 Emissions (Million Metric Tons)": [6.5, 6.6, 6.7, 6.9, 7.0, 7.1, 7.3, 
                                            7.4, 7.6, 7.7, 7.8, 7.9, 8.0, 8.2, 
                                            8.3, 8.4, 8.5, 8.7, 8.8, 8.9, 9.0, 9.1]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
plt.fill_between(df["Year"], df["CO2 Emissions (Million Metric Tons)"], color="#FF6347", alpha=0.7)

plt.title('Annual CO2 Emissions (2000-2021)', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('CO2 Emissions (Million Metric Tons)', fontsize=14)
plt.annotate('Steady Increase', xy=(2010, 7.8), xytext=(2005, 8.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='black')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()