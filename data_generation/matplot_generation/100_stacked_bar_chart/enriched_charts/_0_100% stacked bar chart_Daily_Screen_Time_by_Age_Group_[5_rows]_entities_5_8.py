
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
coal = [40, 37, 34, 31, 28, 25, 22]
natural_gas = [30, 32, 35, 37, 38, 40, 41]
nuclear = [20, 20, 19, 19, 18, 18, 18]
renewables = [10, 11, 12, 13, 16, 17, 19]

# Accumulate the data
totals = [i+j+k+l for i, j, k, l in zip(coal, natural_gas, nuclear, renewables)]
coal_rel = [i / j * 100 for  i, j in zip(coal, totals)]
natural_gas_rel = [i / j * 100 for  i, j in zip(natural_gas, totals)]
nuclear_rel = [i / j * 100 for  i, j in zip(nuclear, totals)]
renewables_rel = [i / j * 100 for  i, j in zip(renewables, totals)]

# Plot
fig, ax = plt.subplots(figsize=(10, 8))

ax.barh(years, coal_rel, color='#1f77b4', edgecolor='white', height=0.85, label='Coal')
ax.barh(years, natural_gas_rel, left=coal_rel, color='#ff7f0e', edgecolor='white', height=0.85, label='Natural Gas')
ax.barh(years, nuclear_rel, left=[i+j for i, j in zip(coal_rel, natural_gas_rel)], color='#2ca02c', edgecolor='white', height=0.85, label='Nuclear')
ax.barh(years, renewables_rel, left=[i+j+k for i, j, k in zip(coal_rel, natural_gas_rel, nuclear_rel)], color='#d62728', edgecolor='white', height=0.85, label='Renewables')

# Adding features to chart
ax.set_xlabel('Percentage')
ax.set_title('Electricity Generation by Source')
plt.xlim(0,100)
leg = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
ax.xaxis.grid(True, which='major', linestyle='--', linewidth='0.5', color='grey')
ax.set_axisbelow(True)

plt.show()