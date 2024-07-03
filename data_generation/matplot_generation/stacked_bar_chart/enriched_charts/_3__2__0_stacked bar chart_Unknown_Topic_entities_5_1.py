
import matplotlib.pyplot as plt

# Data
years = ['2010', '2011', '2012', '2013', '2014', '2015', 
         '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
stocks = [120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]
bonds = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
real_estate = [90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155]
commodities = [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]

# Stacked Bar Chart
plt.figure(figsize=(14, 8))
bar_width = 0.6

plt.bar(years, stocks, color='#4e79a7', edgecolor='white', width=bar_width, label='Stocks')
plt.bar(years, bonds, bottom=stocks, color='#f28e2b', edgecolor='white', width=bar_width, label='Bonds')
plt.bar(years, real_estate, bottom=[i+j for i,j in zip(stocks, bonds)], color='#e15759', edgecolor='white', width=bar_width, label='Real Estate')
plt.bar(years, commodities, bottom=[i+j+k for i,j,k in zip(stocks, bonds, real_estate)], color='#76b7b2', edgecolor='white', width=bar_width, label='Commodities')

for i, (stock, bond, real, comm) in enumerate(zip(stocks, bonds, real_estate, commodities)):
    plt.text(i, stock / 2, str(stock), ha='center', va='center', color='white')
    plt.text(i, stock + bond / 2, str(bond), ha='center', va='center', color='white')
    plt.text(i, stock + bond + real / 2, str(real), ha='center', va='center', color='white')
    plt.text(i, stock + bond + real + comm / 2, str(comm), ha='center', va='center', color='white')

plt.ylabel('Investment in Million USD')
plt.title('Annual Investment Distribution by Asset Type')
plt.xticks(years, rotation=45)
plt.legend(loc='upper left')

plt.show()