
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
renewable_energy = [4800, 5200, 5400, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 7200, 7400]
non_renewable_energy = [7200, 7500, 7400, 7800, 8000, 8200, 8400, 8600, 8800, 9000, 9200, 9400]
nuclear_energy = [3800, 4200, 4300, 4600, 4700, 4900, 5000, 5200, 5300, 5500, 5600, 5800]

plt.figure(figsize=(16, 10))
plt.stackplot(months, renewable_energy, non_renewable_energy, nuclear_energy, 
              labels=['Renewable Energy', 'Non-Renewable Energy', 'Nuclear Energy'],
              colors=['#ff5733', '#33c3ff', '#f1c40f'])

plt.title('Monthly Energy Consumption in a Region', y=1.05)
plt.xlabel('Month')
plt.ylabel('Energy Consumption (MW)')
plt.legend(loc='upper left')
plt.xticks(rotation=45)

peak_non_renewable = max(non_renewable_energy)
peak_month = months[non_renewable_energy.index(peak_non_renewable)]
plt.annotate(f'Peak Non-Renewable Energy\n{peak_non_renewable} MW',
             xy=(peak_month, peak_non_renewable),
             xytext=(peak_month, peak_non_renewable + 1000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

plt.tight_layout()
plt.show()