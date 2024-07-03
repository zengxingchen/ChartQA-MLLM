
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
solar = [8000, 9000, 11000, 13000, 15000, 17000, 19000]
wind = [12000, 13000, 14000, 16000, 17000, 19000, 21000]
hydro = [15000, 16000, 17000, 19000, 21000, 23000, 25000]

# Bottom data for stacking
wind_bottom = solar
hydro_bottom = [i + j for i, j in zip(solar, wind)]

# Figure and Axes
fig, ax = plt.subplots(figsize=(10, 14))  # Change width and height of the chart

# Stacked Bars
ax.barh(years, solar, color='#FFD700', edgecolor='white', height=0.6)  # Solar with gold color
ax.barh(years, wind, left=wind_bottom, color='#1E90FF', edgecolor='white', height=0.6)  # Wind with dodger blue color
ax.barh(years, hydro, left=hydro_bottom, color='#32CD32', edgecolor='white', height=0.6)  # Hydro with lime green color

# Labels and Title
ax.set_xlabel('Energy Produced (in GWh)')
ax.set_ylabel('Year')
ax.set_title('Renewable Energy Production by Type from 2015 to 2021', pad=20)

# Add numerical labels
for i in range(len(years)):
    ax.text(solar[i] / 2, i, str(solar[i]), ha='center', va='center', color='black')
    ax.text(wind_bottom[i] + wind[i] / 2, i, str(wind[i]), ha='center', va='center', color='black')
    ax.text(hydro_bottom[i] + hydro[i] / 2, i, str(hydro[i]), ha='center', va='center', color='black')

# Display the plot
plt.show()