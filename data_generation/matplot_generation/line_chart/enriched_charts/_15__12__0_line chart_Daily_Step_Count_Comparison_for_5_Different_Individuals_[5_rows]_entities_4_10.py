
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
electricity_consumption_kWh = [450, 460, 470, 480, 490, 500, 510, 500, 490, 480, 470, 460]

# Changes to data to enrich visualization (slightly higher July and lower December for example)
electricity_consumption_kWh[6] += 10  # July
electricity_consumption_kWh[-1] -= 10  # December

# Modify color scheme with color codes, change figure size, change trend by increasing the consumption
plt.figure(figsize=(10, 6))
plt.plot(months, [cons - 50 for cons in electricity_consumption_kWh], color='#1f77b4', marker='s')  # Decrease trend with color code

# Adding labels with annotations
for i, (month, cons) in enumerate(zip(months, electricity_consumption_kWh)):
    decreased_cons = cons - 50
    plt.annotate(f'{cons} kWh', (month, decreased_cons), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Monthly Electricity Consumption with Decreased Trend')
plt.xlabel('Month')
plt.ylabel('Electricity Consumption (kWh)')
plt.gca().invert_yaxis()

# Display chart
plt.show()