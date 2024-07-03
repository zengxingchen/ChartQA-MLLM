
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
rent = [700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810]
groceries = [520, 500, 480, 470, 490, 510, 530, 550, 570, 560, 550, 540]
utilities = [210, 220, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140]
entertainment = [120, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20]

total = [sum(x) for x in zip(rent, groceries, utilities, entertainment)]
rent_percent = [i / j * 100 for i, j in zip(rent, total)]
groceries_percent = [i / j * 100 for i, j in zip(groceries, total)]
utilities_percent = [i / j * 100 for i, j in zip(utilities, total)]
entertainment_percent = [i / j * 100 for i, j in zip(entertainment, total)]

r = range(len(months))

fig, ax = plt.subplots(figsize=(10, 16))

barWidth = 0.65
ax.bar(r, rent_percent, color='#FF6347', edgecolor='white', width=barWidth, label="Rent")
ax.bar(r, groceries_percent, bottom=rent_percent, color='#4682B4', edgecolor='white', width=barWidth, label="Groceries")
ax.bar(r, utilities_percent, bottom=[i + j for i, j in zip(rent_percent, groceries_percent)], color='#32CD32', edgecolor='white', width=barWidth, label="Utilities")
ax.bar(r, entertainment_percent, bottom=[i + j + k for i, j, k in zip(rent_percent, groceries_percent, utilities_percent)], color='#FFD700', edgecolor='white', width=barWidth, label="Entertainment")

plt.xticks(r, months, rotation=45)
plt.ylabel("Percentage")
plt.title("Monthly Distribution of Household Expenses (Percentage)", pad=20)

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4, title="Categories")

plt.show()