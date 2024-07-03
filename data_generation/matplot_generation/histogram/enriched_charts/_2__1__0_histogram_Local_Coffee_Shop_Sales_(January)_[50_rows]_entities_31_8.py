
import matplotlib.pyplot as plt

# Data points
sleep_hours = [
    6.5, 7.0, 6.0, 8.0, 5.5, 7.5, 6.8, 7.2, 6.3, 8.1, 5.8, 7.9, 6.1, 6.7, 8.3, 5.9, 6.4, 7.6, 5.4, 7.3, 
    6.6, 6.2, 7.8, 5.7, 7.4, 8.2, 6.9, 5.6, 7.1, 6.7, 5.3, 8.4, 6.2, 7.7, 6.1, 5.8, 7.0, 6.4, 5.6, 8.0, 
    7.5, 6.3, 7.2, 6.5, 7.9, 5.7, 6.8, 8.1, 5.5, 7.6
]

plt.figure(figsize=(10, 6))  # Change width and height of the chart
n, bins, patches = plt.hist(sleep_hours, bins=8, color='#1F77B4', rwidth=0.7)  # Changing color and making histogram horizontal.

# Setting the colors of individual bars (patches)
for patch in patches:
    patch.set_facecolor('#FF7F0E')  # A nice orange color

# Add a black line at the edge of each bar
[patch.set_linewidth(0.7) for patch in patches]
[patch.set_edgecolor('#000000') for patch in patches]

plt.title('Distribution of Sleep Hours per Night', pad=20)
plt.xlabel('Frequency')
plt.ylabel('Hours of Sleep')
plt.grid(True)
plt.gca().invert_yaxis()  # Making the histogram horizontal
plt.show()