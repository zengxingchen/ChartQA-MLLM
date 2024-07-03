
import matplotlib.pyplot as plt
import numpy as np

categories = ['2019', '2020', '2021', '2022']
cardio = [15, 20, 25, 30]
strength = [20, 25, 30, 35]
flexibility = [10, 15, 20, 25]
balance = [5, 10, 15, 20]
mind_body = [50, 30, 10, 10]

barWidth = 0.85
bars1 = np.array(cardio)
bars2 = np.array(strength)
bars3 = np.array(flexibility)
bars4 = np.array(balance)
bars5 = np.array(mind_body)

r = np.arange(len(categories))

plt.figure(figsize=(10, 6))
plt.bar(r, bars1, color='#FF5733', edgecolor='grey', width=barWidth, label='Cardio Exercise')
plt.bar(r, bars2, bottom=bars1, color='#33FF57', edgecolor='grey', width=barWidth, label='Strength Training')
plt.bar(r, bars3, bottom=bars1+bars2, color='#3357FF', edgecolor='grey', width=barWidth, label='Flexibility')
plt.bar(r, bars4, bottom=bars1+bars2+bars3, color='#F4C300', edgecolor='grey', width=barWidth, label='Balance')
plt.bar(r, bars5, bottom=bars1+bars2+bars3+bars4, color='#C70039', edgecolor='grey', width=barWidth, label='Mind & Body')

plt.xlabel('Year')
plt.ylabel('Percentage')
plt.title('Trends in Exercise Types Over Years', pad=20)
plt.xticks(r, categories)
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
plt.show()