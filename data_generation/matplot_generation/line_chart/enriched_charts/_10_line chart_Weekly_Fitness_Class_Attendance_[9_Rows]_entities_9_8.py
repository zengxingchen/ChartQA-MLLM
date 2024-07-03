
import matplotlib.pyplot as plt

data = [
    {'Week': '2023-W10', 'Electric Cars': 15, 'Hybrid Cars': 30, 'Diesel Cars': 25, 'Petrol Cars': 40},
    {'Week': '2023-W11', 'Electric Cars': 18, 'Hybrid Cars': 35, 'Diesel Cars': 22, 'Petrol Cars': 38},
    {'Week': '2023-W12', 'Electric Cars': 20, 'Hybrid Cars': 32, 'Diesel Cars': 24, 'Petrol Cars': 35},
    {'Week': '2023-W13', 'Electric Cars': 22, 'Hybrid Cars': 34, 'Diesel Cars': 27, 'Petrol Cars': 37},
    {'Week': '2023-W14', 'Electric Cars': 25, 'Hybrid Cars': 38, 'Diesel Cars': 30, 'Petrol Cars': 40},
    {'Week': '2023-W15', 'Electric Cars': 28, 'Hybrid Cars': 35, 'Diesel Cars': 33, 'Petrol Cars': 42},
    {'Week': '2023-W16', 'Electric Cars': 30, 'Hybrid Cars': 37, 'Diesel Cars': 35, 'Petrol Cars': 45},
    {'Week': '2023-W17', 'Electric Cars': 32, 'Hybrid Cars': 40, 'Diesel Cars': 38, 'Petrol Cars': 43},
    {'Week': '2023-W18', 'Electric Cars': 35, 'Hybrid Cars': 42, 'Diesel Cars': 40, 'Petrol Cars': 46},
    {'Week': '2023-W19', 'Electric Cars': 37, 'Hybrid Cars': 45, 'Diesel Cars': 42, 'Petrol Cars': 48},
    {'Week': '2023-W20', 'Electric Cars': 40, 'Hybrid Cars': 47, 'Diesel Cars': 45, 'Petrol Cars': 50}
]

weeks = [entry['Week'] for entry in data]
electric_cars = [entry['Electric Cars'] for entry in data]
hybrid_cars = [entry['Hybrid Cars'] for entry in data]
diesel_cars = [entry['Diesel Cars'] for entry in data]
petrol_cars = [entry['Petrol Cars'] for entry in data]

plt.figure(figsize=(12, 8))

plt.plot(weeks, electric_cars, marker='o', linestyle='-', color='#1f77b4', label='Electric Cars')
plt.plot(weeks, hybrid_cars, marker='x', linestyle='--', color='#ff7f0e', label='Hybrid Cars')
plt.plot(weeks, diesel_cars, marker='s', linestyle='-.', color='#2ca02c', label='Diesel Cars')
plt.plot(weeks, petrol_cars, marker='^', linestyle=':', color='#d62728', label='Petrol Cars')

plt.title('Car Sales Trends Over Weeks', fontsize=14, pad=20)
plt.xlabel('Week')
plt.ylabel('Number of Cars Sold')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.tight_layout()

for i, txt in enumerate(electric_cars):
    plt.annotate(txt, (weeks[i], electric_cars[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='#1f77b4')
for i, txt in enumerate(hybrid_cars):
    plt.annotate(txt, (weeks[i], hybrid_cars[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='#ff7f0e')
for i, txt in enumerate(diesel_cars):
    plt.annotate(txt, (weeks[i], diesel_cars[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='#2ca02c')
for i, txt in enumerate(petrol_cars):
    plt.annotate(txt, (weeks[i], petrol_cars[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='#d62728')

plt.show()