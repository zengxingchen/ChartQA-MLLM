
import matplotlib.pyplot as plt

years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
protein = [25, 28, 30, 32, 35, 37, 38, 40, 42, 45]
carbohydrates = [40, 38, 36, 34, 32, 30, 28, 25, 22, 20]
fat = [20, 22, 25, 27, 25, 26, 25, 25, 27, 25]
vitamins = [15, 12, 9, 7, 8, 7, 9, 10, 9, 10]

totals = [i + j + k + l for i, j, k, l in zip(protein, carbohydrates, fat, vitamins)]
protein_rel = [i / j * 100 for i, j in zip(protein, totals)]
carbohydrates_rel = [i / j * 100 for i, j in zip(carbohydrates, totals)]
fat_rel = [i / j * 100 for i, j in zip(fat, totals)]
vitamins_rel = [i / j * 100 for i, j in zip(vitamins, totals)]

fig, ax = plt.subplots(figsize=(12, 10))

ax.bar(years, protein_rel, color='#4B0082', edgecolor='white', width=0.75, label='Protein')
ax.bar(years, carbohydrates_rel, bottom=protein_rel, color='#FFD700', edgecolor='white', width=0.75, label='Carbohydrates')
ax.bar(years, fat_rel, bottom=[i + j for i, j in zip(protein_rel, carbohydrates_rel)], color='#228B22', edgecolor='white', width=0.75, label='Fat')
ax.bar(years, vitamins_rel, bottom=[i + j + k for i, j, k in zip(protein_rel, carbohydrates_rel, fat_rel)], color='#FF4500', edgecolor='white', width=0.75, label='Vitamins')

ax.set_ylabel('Percentage')
ax.set_title('Nutritional Composition by Year')
plt.ylim(0, 100)
leg = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), shadow=True, ncol=2)
ax.yaxis.grid(True, which='major', linestyle='--', linewidth='0.5', color='grey')
ax.set_axisbelow(True)

plt.show()