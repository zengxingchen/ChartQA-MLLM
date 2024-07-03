
import matplotlib.pyplot as plt

# Your data
data = [
    {'Month': 'January', 'Bikes Rented': 805},
    {'Month': 'February', 'Bikes Rented': 670},
    {'Month': 'March', 'Bikes Rented': 945},
    {'Month': 'April', 'Bikes Rented': 1134},
    {'Month': 'May', 'Bikes Rented': 1417},
    {'Month': 'June', 'Bikes Rented': 1673},
    {'Month': 'July', 'Bikes Rented': 1724},
    {'Month': 'August', 'Bikes Rented': 1660},
    {'Month': 'September', 'Bikes Rented': 1532},
    {'Month': 'October', 'Bikes Rented': 1284},
    {'Month': 'November', 'Bikes Rented': 980},
    {'Month': 'December', 'Bikes Rented': 859}
]

# Parsing data for plotting
months = [entry['Month'] for entry in data]
rentals = [entry['Bikes Rented'] for entry in data]

# Plotting the area chart
plt.figure(figsize=(12, 6))
plt.fill_between(months, rentals, color="skyblue", alpha=0.4)
plt.plot(months, rentals, color="Slateblue", alpha=0.6, linewidth=2, linestyle='dashed', marker='o', markersize=8)

# Customizing the grid
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# Adding titles and labels
plt.title('Bike Rentals Per Month', fontsize=18, fontweight='bold')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Bikes Rented', fontsize=14)

# Adding a marker for the highest value
max_rental = max(rentals)
max_month = months[rentals.index(max_rental)]
plt.annotate(f'Peak\n{max_rental}', xy=(max_month, max_rental), xytext=(max_month, max_rental+100),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center', verticalalignment='bottom')

plt.tight_layout()
plt.show()