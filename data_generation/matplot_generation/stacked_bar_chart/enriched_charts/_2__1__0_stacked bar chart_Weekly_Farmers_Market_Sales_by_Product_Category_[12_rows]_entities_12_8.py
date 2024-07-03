
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
renewable_energy = [450, 470, 490, 510, 530, 550, 570, 590, 610, 630, 650, 670]
carbon_emissions = [800, 820, 840, 860, 880, 900, 920, 940, 960, 980, 1000, 1020]
electric_vehicles = [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410]
green_investments = [250, 270, 290, 310, 330, 350, 370, 390, 410, 430, 450, 470]
public_transport = [100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320]

# Stacked Bar Chart
fig, ax = plt.subplots(figsize=(14, 10))

bar_height = 0.5
index = range(len(months))

p1 = plt.barh(index, renewable_energy, bar_height, label='Renewable Energy', color='#76B041')
p2 = plt.barh(index, carbon_emissions, bar_height, left=renewable_energy, label='Carbon Emissions', color='#F28D35')
p3 = plt.barh(index, electric_vehicles, bar_height, left=[r + c for r, c in zip(renewable_energy, carbon_emissions)], label='Electric Vehicles', color='#3498DB')
p4 = plt.barh(index, green_investments, bar_height, left=[r + c + e for r, c, e in zip(renewable_energy, carbon_emissions, electric_vehicles)], label='Green Investments', color='#8E44AD')
p5 = plt.barh(index, public_transport, bar_height, left=[r + c + e + g for r, c, e, g in zip(renewable_energy, carbon_emissions, electric_vehicles, green_investments)], label='Public Transport', color='#F1C40F')

plt.xlabel('Expenses in USD')
plt.yticks(index, months)
plt.title('Monthly Environmental Investments')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), shadow=True, ncol=1)

# Customizing the grid
plt.grid(axis='x')

plt.show()