
import matplotlib.pyplot as plt

# Data points
temperatures = [
    12, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24,
    25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 34,
    35, 36, 37, 37, 38, 39, 40, 41
]

plt.figure(figsize=(10,6))  # Change width and height of the chart
n, bins, patches = plt.hist(temperatures, bins=15, color='#3498db', orientation='horizontal', rwidth=0.9)  # Changing color and making histogram horizontal.

# Setting the colors of individual bars (patches)
for patch in patches:
    patch.set_facecolor('#48C9B0')  # A nice teal color

# Add a black line at the edge of each bar
[patch.set_linewidth(0.5) for patch in patches]
[patch.set_edgecolor('#000000') for patch in patches]

plt.title('Temperature Distribution over a Period')
plt.xlabel('Frequency')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()