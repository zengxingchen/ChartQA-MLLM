
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Year": [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    "Annual Average Rainfall (mm)": [1200, 1185, 1210, 1195, 1220, 1175, 1150, 
                                     1160, 1190, 1170, 1205, 1180, 1165, 1175, 
                                     1215, 1190, 1180, 1170, 1155, 1165, 1145, 1130]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
plt.fill_between(df["Year"], df["Annual Average Rainfall (mm)"], color="#8A2BE2", alpha=0.7)

plt.title('Annual Average Rainfall in Region X (2000-2021)', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Annual Average Rainfall (mm)', fontsize=14)
plt.annotate('Significant Decrease', xy=(2016, 1180), xytext=(2011, 1200),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='black')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()