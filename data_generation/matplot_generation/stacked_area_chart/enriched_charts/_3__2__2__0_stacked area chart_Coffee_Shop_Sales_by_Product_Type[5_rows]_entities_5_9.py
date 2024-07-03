
import matplotlib.pyplot as plt

# Table data of monthly activities
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
urban_population = [7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000, 8100]
rural_population = [12000, 12100, 12200, 12300, 12400, 12500, 12600, 12700, 12800, 12900, 13000, 13100]
forest_area = [8000, 8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000, 9100]
water_bodies = [3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100]

# Stacked area chart
plt.figure(figsize=(18, 12))
plt.stackplot(months, urban_population, rural_population, forest_area, water_bodies, 
              labels=['Urban Population', 'Rural Population', 'Forest Area', 'Water Bodies'],
              colors=['#FF6347', '#4682B4', '#3CB371', '#FFD700'])

# Customizing the plot with titles, labels and annotations
plt.title('Monthly Environmental Changes in 2024', fontsize=20)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Area / Population', fontsize=16)
plt.legend(loc='upper left')
plt.xticks(rotation=45, fontsize=14)

# Annotation example
peak_forest_area = max(forest_area)
peak_month = months[forest_area.index(peak_forest_area)]
plt.annotate(f'Peak Forest Area\n{peak_forest_area} sq km',
             xy=(peak_month, peak_forest_area),
             xytext=(peak_month, peak_forest_area + 3000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

plt.tight_layout()
plt.show()