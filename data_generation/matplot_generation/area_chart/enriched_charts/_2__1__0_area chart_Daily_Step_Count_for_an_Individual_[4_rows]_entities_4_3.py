
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Year": [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    "Global Forest Area (Million Hectares)": [4200, 4185, 4170, 4155, 4140, 4120, 4100, 
                                              4080, 4060, 4040, 4020, 4000, 3985, 3970, 
                                              3955, 3940, 3925, 3910, 3895, 3880, 3865, 3850]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
plt.fill_between(df["Year"], df["Global Forest Area (Million Hectares)"], color="#4682B4", alpha=0.7)

plt.title('Global Forest Area (2000-2021)', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Global Forest Area (Million Hectares)', fontsize=14)
plt.annotate('Decreasing Trend', xy=(2010, 4020), xytext=(2005, 4100),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='black')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()