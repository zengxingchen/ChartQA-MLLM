
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
co2_emissions = [400, 410, 420, 430, 450, 470, 490, 480, 460, 440, 420, 410]
solar_power = [200, 210, 220, 230, 250, 270, 290, 280, 260, 240, 220, 210]
wind_power = [150, 160, 170, 180, 200, 220, 240, 230, 210, 190, 170, 160]

# Stacked Area Chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(months, co2_emissions, solar_power, wind_power, colors=['#8B0000', '#FFD700', '#00BFFF'])

# Customizing the plot
ax.set_title('Monthly Environmental Data in 2023')
ax.set_ylabel('Values')
ax.set_xlabel('Month')
ax.margins(0, 0)  # Removes the default margins to use the entire space for plotting

# Adding annotation
ax.annotate('CO2 Emissions peak', xy=('July', 490), xytext=('August', 520),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Displaying the plot
plt.show()