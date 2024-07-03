
import matplotlib.pyplot as plt
import numpy as np

categories = ['2019', '2020', '2021', '2022', '2023', '2024']
fruits = [30, 25, 20, 15, 10, 5]
vegetables = [20, 25, 30, 35, 40, 45]
grains = [20, 20, 20, 20, 20, 20]
protein = [15, 15, 15, 15, 15, 15]
dairy = [15, 15, 15, 15, 15, 15]

barWidth = 0.7
bars1 = np.array(fruits)
bars2 = np.array(vegetables)
bars3 = np.array(grains)
bars4 = np.array(protein)
bars5 = np.array(dairy)

r = np.arange(len(categories))

plt.figure(figsize=(12, 8))
plt.bar(r, bars1, color='#FF5733', edgecolor='grey', width=barWidth, label='Fruits')
plt.bar(r, bars2, bottom=bars1, color='#33FF57', edgecolor='grey', width=barWidth, label='Vegetables')
plt.bar(r, bars3, bottom=bars1+bars2, color='#3357FF', edgecolor='grey', width=barWidth, label='Grains')
plt.bar(r, bars4, bottom=bars1+bars2+bars3, color='#F4C300', edgecolor='grey', width=barWidth, label='Protein')
plt.bar(r, bars5, bottom=bars1+bars2+bars3+bars4, color='#C70039', edgecolor='grey', width=barWidth, label='Dairy')

plt.xlabel('Year')
plt.ylabel('Percentage')
plt.title('Trends in Food Consumption Over Years', pad=20)
plt.xticks(r, categories)
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
plt.show()