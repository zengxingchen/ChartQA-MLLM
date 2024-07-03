import matplotlib.pyplot as plt

data = [
    {'Day': 'Monday', 'Person A': 12000, 'Person B': 14000, 'Person C': 8000, 'Person D': 10000, 'Person E': 9000},
    {'Day': 'Tuesday', 'Person A': 13000, 'Person B': 13500, 'Person C': 8500, 'Person D': 9500, 'Person E': 8500},
    {'Day': 'Wednesday', 'Person A': 11500, 'Person B': 13000, 'Person C': 7500, 'Person D': 11000, 'Person E': 10000},
    {'Day': 'Thursday', 'Person A': 14000, 'Person B': 14500, 'Person C': 9500, 'Person D': 12000, 'Person E': 10500},
    {'Day': 'Friday', 'Person A': 15000, 'Person B': 15000, 'Person C': 10000, 'Person D': 13000, 'Person E': 11000},
    {'Day': 'Saturday', 'Person A': 16000, 'Person B': 16000, 'Person C': 11000, 'Person D': 14000, 'Person E': 11500},
    {'Day': 'Sunday', 'Person A': 15500, 'Person B': 15500, 'Person C': 10500, 'Person D': 13500, 'Person E': 12000}
]

days = [item['Day'] for item in data]
person_a = [item['Person A'] for item in data]
person_b = [item['Person B'] for item in data]
person_c = [item['Person C'] for item in data]
person_d = [item['Person D'] for item in data]
person_e = [item['Person E'] for item in data]

plt.figure(figsize=(12, 8))
plt.plot(days, person_a, label='Person A', linestyle='-', marker='o', color='#1f77b4')
plt.plot(days, person_b, label='Person B', linestyle='--', marker='s', color='#ff7f0e')
plt.plot(days, person_c, label='Person C', linestyle='-.', marker='^', color='#2ca02c')
plt.plot(days, person_d, label='Person D', linestyle=':', marker='D', color='#d62728')
plt.plot(days, person_e, label='Person E', linestyle='-', marker='*', color='#9467bd')

plt.title('Weekly Step Count for Different Individuals', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Number of Steps')
plt.legend(loc='upper left')

plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
plt.gca().invert_yaxis()

for i, txt in enumerate(person_d):
    plt.annotate(txt, (days[i], person_d[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()