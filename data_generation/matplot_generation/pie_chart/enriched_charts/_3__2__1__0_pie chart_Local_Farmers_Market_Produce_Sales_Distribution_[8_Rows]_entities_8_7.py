
import matplotlib.pyplot as plt

# Data
destinations = ["Beaches", "Mountains", "Cities", "Countryside", "Deserts", "Forests", "Islands", "Lakes", "Historical Sites"]
number_of_visitors = [30, 25, 20, 15, 10, 12, 18, 8, 22]

# Colors
colors = [
    "#FF6347",  # Beaches
    "#4682B4",  # Mountains
    "#FFD700",  # Cities
    "#32CD32",  # Countryside
    "#8B4513",  # Deserts
    "#2E8B57",  # Forests
    "#00CED1",  # Islands
    "#1E90FF",  # Lakes
    "#FF69B4",  # Historical Sites
]

# Create pie chart
plt.figure(figsize=(14, 12))  # width and height in inches
plt.pie(number_of_visitors, labels=destinations, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Annual Tourist Visits by Destination Type', pad=30)

# Show plot
plt.show()