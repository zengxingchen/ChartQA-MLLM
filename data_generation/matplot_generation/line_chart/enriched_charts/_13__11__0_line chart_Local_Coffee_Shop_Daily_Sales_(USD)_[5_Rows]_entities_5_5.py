
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
passing_percentage = [85, 88, 84, 87, 90, 85, 82, 78, 80, 88, 91, 85]

# Plotting the line chart
plt.figure(figsize=(12, 8))
plt.plot(months, passing_percentage, marker='o', linestyle='-', color='#1f77b4', linewidth=2.5)

# Adding title and labels
plt.title('Monthly Passing Percentage of Students in School ABC', fontsize=18)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Passing Percentage (%)', fontsize=12)

# Adding an annotation for the highest passing percentage
highest_passing_index = passing_percentage.index(max(passing_percentage))
highest_passing_month = months[highest_passing_index]
plt.annotate('Highest', xy=(highest_passing_index, max(passing_percentage)), xytext=(highest_passing_index, max(passing_percentage) + 2),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(75, 95)
plt.show()