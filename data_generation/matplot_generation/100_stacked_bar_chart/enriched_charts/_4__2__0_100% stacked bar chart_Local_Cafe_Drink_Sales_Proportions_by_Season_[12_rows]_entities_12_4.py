
import matplotlib.pyplot as plt
import numpy as np

categories = ['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Australia', 'Antarctica']
brand_a = [25, 30, 20, 15, 10, 40, 35]
brand_b = [40, 35, 25, 30, 20, 25, 30]
brand_c = [35, 35, 55, 55, 70, 35, 35]

barWidth = 0.4

r = np.arange(len(categories))

plt.figure(figsize=(10, 14))

plt.bar(r, brand_a, color='#FF5733', edgecolor='grey', width=barWidth, label='Brand A')
plt.bar(r, brand_b, bottom=brand_a, color='#33FF57', edgecolor='grey', width=barWidth, label='Brand B')
plt.bar(r, brand_c, bottom=np.add(brand_a, brand_b), color='#3357FF', edgecolor='grey', width=barWidth, label='Brand C')

plt.ylabel('Percentage')
plt.xlabel('Regions')
plt.title('Distribution of Sales by Brand in Different Regions')
plt.xticks(r, categories, rotation=45)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()