
import matplotlib.pyplot as plt

# Data for the chart
operating_systems = ['Android', 'iOS', 'KaiOS', 'Samsung', 'HarmonyOS', 'Other']
market_shares = [70, 27, 1, 0.5, 0.5, 1]
colors = ['#FFA726', '#4DB6AC', '#FFEE58', '#29B6F6', '#AB47BC', '#78909C']

# Create a pie chart
plt.figure(figsize=(8, 8)) # Set the width and height of the chart
plt.pie(market_shares, labels=operating_systems, autopct='%1.1f%%', colors=colors, startangle=140)

plt.title('Global Smartphone OS Market Share in 2023') # Change the headline to match the topic
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()