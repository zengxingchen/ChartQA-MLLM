
import matplotlib.pyplot as plt

# Data
years = ['2010', '2011', '2012', '2013', '2014', '2015', 
         '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
renewable_energy = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330]
non_renewable_energy = [300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170]
nuclear_energy = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280]
hydroelectric_energy = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230]

# Stacked Bar Chart
plt.figure(figsize=(16, 10))
bar_height = 0.6

plt.barh(years, renewable_energy, color='#1f77b4', edgecolor='white', height=bar_height, label='Renewable Energy')
plt.barh(years, non_renewable_energy, left=renewable_energy, color='#ff7f0e', edgecolor='white', height=bar_height, label='Non-Renewable Energy')
plt.barh(years, nuclear_energy, left=[i+j for i,j in zip(renewable_energy, non_renewable_energy)], color='#2ca02c', edgecolor='white', height=bar_height, label='Nuclear Energy')
plt.barh(years, hydroelectric_energy, left=[i+j+k for i,j,k in zip(renewable_energy, non_renewable_energy, nuclear_energy)], color='#d62728', edgecolor='white', height=bar_height, label='Hydroelectric Energy')

for i, (renew, non_renew, nucl, hydro) in enumerate(zip(renewable_energy, non_renewable_energy, nuclear_energy, hydroelectric_energy)):
    plt.text(renew / 2, i, str(renew), ha='center', va='center', color='white')
    plt.text(renew + non_renew / 2, i, str(non_renew), ha='center', va='center', color='white')
    plt.text(renew + non_renew + nucl / 2, i, str(nucl), ha='center', va='center', color='white')
    plt.text(renew + non_renew + nucl + hydro / 2, i, str(hydro), ha='center', va='center', color='white')

plt.xlabel('Energy Production in Gigawatt Hours')
plt.title('Annual Energy Production by Type')
plt.yticks(years)
plt.legend(loc='upper right')

plt.show()