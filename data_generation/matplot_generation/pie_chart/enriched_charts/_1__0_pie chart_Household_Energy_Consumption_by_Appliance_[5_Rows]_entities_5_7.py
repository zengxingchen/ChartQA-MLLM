
import matplotlib.pyplot as plt

# Data
destinations = [
    'Europe', 'Asia', 'North America', 'South America', 'Africa', 
    'Oceania', 'Antarctica'
]
percentages = [35.4, 28.3, 18.5, 7.6, 5.1, 3.5, 1.6]

# Colors
colors = [
    '#2E86C1', '#AF7AC5', '#F4D03F', '#58D68D', '#E74C3C', 
    '#5DADE2', '#EB984E'
]

# Plot
plt.figure(figsize=(12, 9))  # Width and height of the chart
plt.pie(percentages, labels=destinations, colors=colors, startangle=90, autopct='%1.1f%%')

plt.title("Preferred Travel Destinations in 2023")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()