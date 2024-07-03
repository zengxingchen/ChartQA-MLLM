
import matplotlib.pyplot as plt

# Generate data points
days = list(range(1, 31))
energy_consumption_kWh = [
    150, 165, 170, 180, 200, 220, 230, 215, 235, 240,
    255, 260, 270, 280, 300, 320, 340, 360, 370, 380,
    390, 400, 420, 430, 440, 460, 480, 500, 520, 550
]

# Create an area chart
plt.figure(figsize=(12, 6))  # Changed width and height
plt.fill_between(days, energy_consumption_kWh, color="#4E9A06")  # Modified color scheme

# Customize axes and labels
plt.title("Daily Energy Consumption for a Small Community")
plt.xlabel("Day of the Month")
plt.ylabel("Energy Consumption (kWh)")
plt.xticks(range(1, 31, 2))  # Show every second day for clarity
plt.yticks(range(100, 601, 50))  # Adjust the y-ticks to cover the data range

# Display the plot
plt.show()