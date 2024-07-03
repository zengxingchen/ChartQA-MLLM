
import matplotlib.pyplot as plt

ages = [
    22, 25, 28, 33, 35, 37, 39, 40, 41, 42, 44, 45, 46, 48, 50, 52, 55, 56, 58, 60, 62, 64, 66, 68, 70, 72, 75, 77, 79, 80, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 100
]

bins = [20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.figure(figsize=(8, 12)) # Width and height of the chart
plt.hist(ages, bins=bins, color='#FF6347', edgecolor='black', linewidth=1.5, orientation='vertical')

plt.title('Age Distribution of Conference Attendees')
plt.ylabel('Frequency')
plt.xlabel('Ages')

plt.xticks([25, 35, 45, 55, 65, 75, 85, 95])

plt.show()