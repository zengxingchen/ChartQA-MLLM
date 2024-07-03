
import matplotlib.pyplot as plt

countries = [
    "Brazil", "Indonesia", "China", "Peru", "Mexico",
    "Australia", "India", "Colombia", "Ecuador", 
    "United States", "Madagascar", "Philippines", 
    "Papua New Guinea", "Thailand", "Congo", "Vietnam"
]
species_discovered = [
    20000, 18000, 16000, 15000, 14000,
    13000, 12500, 12000, 11500, 11000,
    10500, 10000, 9500, 9000, 8500, 8000
]

colors = [
    '#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f',
    '#e67e22', '#1abc9c', '#34495e', '#d35400', '#c0392b',
    '#7f8c8d', '#2980b9', '#8e44ad', '#27ae60', '#f39c12',
    '#16a085'
]

plt.figure(figsize=(12, 10))
plt.bar(countries, species_discovered, color=colors, width=0.5)

plt.ylim(7000, 21000)
plt.title('Number of Species Discovered in Various Countries', fontsize=18, pad=30)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Number of Species Discovered', fontsize=14)

plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()
plt.show()