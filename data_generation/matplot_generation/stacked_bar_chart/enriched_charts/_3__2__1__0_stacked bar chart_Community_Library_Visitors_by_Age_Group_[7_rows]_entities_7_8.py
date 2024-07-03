
import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'])
Cardio = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])
Strength = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])
Flexibility = np.array([15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
Balance = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

bar_width = 0.35
fig, ax = plt.subplots(figsize=(14, 10))

ax.bar(years, Cardio, width=bar_width, label='Cardio', color='#FF6347')
ax.bar(years, Strength, bottom=Cardio, width=bar_width, label='Strength', color='#4682B4')
ax.bar(years, Flexibility, bottom=Cardio+Strength, width=bar_width, label='Flexibility', color='#32CD32')
ax.bar(years, Balance, bottom=Cardio+Strength+Flexibility, width=bar_width, label='Balance', color='#FFD700')

ax.set_ylabel('Hours of Exercise')
ax.set_title('Annual Exercise Routine (2010-2024)', pad=20)
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45)
ax.legend(ncol=1, loc='upper left', bbox_to_anchor=(1, 1))

for i in range(len(years)):
    ax.text(i, Cardio[i] / 2, str(Cardio[i]), ha='center', va='center', color='white', fontsize=9)
    ax.text(i, Cardio[i] + Strength[i] / 2, str(Strength[i]), ha='center', va='center', color='white', fontsize=9)
    ax.text(i, Cardio[i] + Strength[i] + Flexibility[i] / 2, str(Flexibility[i]), ha='center', va='center', color='white', fontsize=9)
    ax.text(i, Cardio[i] + Strength[i] + Flexibility[i] + Balance[i] / 2, str(Balance[i]), ha='center', va='center', color='white', fontsize=9)

plt.tight_layout()
plt.show()