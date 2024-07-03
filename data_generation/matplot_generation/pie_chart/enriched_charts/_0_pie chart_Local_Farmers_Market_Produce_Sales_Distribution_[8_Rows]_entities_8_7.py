
import matplotlib.pyplot as plt

# Data
energy_sources = ["Oil", "Natural Gas", "Coal", "Nuclear", "Hydro", "Wind", "Solar", "Biofuels", "Others"]
consumption = [180, 130, 120, 70, 90, 50, 40, 30, 10]

# Colors
colors = [
    "#FF5733",  # Oil
    "#C70039",  # Natural Gas
    "#900C3F",  # Coal
    "#581845",  # Nuclear
    "#2e8b57",  # Hydro
    "#4682b4",  # Wind
    "#ffdaB9",  # Solar
    "#ffa500",  # Biofuels
    "#808080",  # Others
]

# Create pie chart
plt.figure(figsize=(12, 7))  # width and height in inches
plt.pie(consumption, labels=energy_sources, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Global Energy Consumption by Source in 2020', pad=20)

# Show plot
plt.show()