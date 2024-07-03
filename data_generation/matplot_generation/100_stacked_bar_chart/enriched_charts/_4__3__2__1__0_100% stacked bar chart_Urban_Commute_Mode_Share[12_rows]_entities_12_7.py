
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Year': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025'],
    'Stocks': [30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],
    'Bonds': [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15],
    'Real Estate': [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
    'Commodities': [15, 15, 15, 14, 14, 13, 13, 12, 12, 11, 10],
    'Cash': [10, 10, 10, 11, 11, 12, 12, 13, 13, 14, 15]
}

years = data['Year']
stocks = data['Stocks']
bonds = data['Bonds']
real_estate = data['Real Estate']
commodities = data['Commodities']
cash = data['Cash']

# Plotting
fig, ax = plt.subplots(figsize=(14, 10))

bar_width = 0.7

stocks_bar = np.array(stocks)
bonds_bar = np.array(bonds)
real_estate_bar = np.array(real_estate)
commodities_bar = np.array(commodities)
cash_bar = np.array(cash)

bar_positions = np.arange(len(years))

ax.bar(bar_positions, stocks_bar, color='#1F618D', edgecolor='white', width=bar_width, label='Stocks')
ax.bar(bar_positions, bonds_bar, bottom=stocks_bar, color='#2ECC71', edgecolor='white', width=bar_width, label='Bonds')
ax.bar(bar_positions, real_estate_bar, bottom=stocks_bar + bonds_bar, color='#F1C40F', edgecolor='white', width=bar_width, label='Real Estate')
ax.bar(bar_positions, commodities_bar, bottom=stocks_bar + bonds_bar + real_estate_bar, color='#E74C3C', edgecolor='white', width=bar_width, label='Commodities')
ax.bar(bar_positions, cash_bar, bottom=stocks_bar + bonds_bar + real_estate_bar + commodities_bar, color='#9B59B6', edgecolor='white', width=bar_width, label='Cash')

# Customizing the plot
ax.set_xticks(bar_positions)
ax.set_xticklabels(years)
ax.set_ylabel('Percentage')
ax.set_title('Investment Portfolio Distribution Over Years', pad=20)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=5)

plt.tight_layout()
plt.show()