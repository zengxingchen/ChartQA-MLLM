
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
startups = [150, 160, 170, 180, 200, 190, 210, 220, 200, 190, 180, 170]

# Plotting the line chart
plt.figure(figsize=(12, 8))
plt.plot(months, startups, marker='o', linestyle='-', color='#66c2a5', linewidth=2.5)

# Adding title and labels
plt.title('Monthly New Business Startups in City XYZ', fontsize=18)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Startups', fontsize=12)

# Adding an annotation for the highest number of startups
highest_startups_index = startups.index(max(startups))
highest_startups_month = months[highest_startups_index]
plt.annotate('Highest', xy=(highest_startups_index, max(startups)), xytext=(highest_startups_index, max(startups) + 10),
             arrowprops=dict(facecolor='#fc8d62', shrink=0.05))

# Add a grid, invert y-axis and show the plot
plt.grid(True)
plt.ylim(250, 100)
plt.gca().invert_yaxis()
plt.show()