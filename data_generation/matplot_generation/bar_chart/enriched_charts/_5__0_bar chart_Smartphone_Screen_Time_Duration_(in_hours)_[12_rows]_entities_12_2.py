
import matplotlib.pyplot as plt

# Data to plot
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [32, 35, 45, 55, 65, 75, 85, 88, 78, 65, 50, 37]

# Plot a vertical bar chart
plt.figure(figsize=(10, 6))  # Width and height of the chart
plt.bar(x=months, height=temperatures, color=[
    '#4B0082', '#8A2BE2', '#7FFF00', '#D2691E',
    '#FF7F50', '#6495ED', '#DC143C', '#00FFFF',
    '#00008B', '#008B8B', '#B8860B', '#A9A9A9'],
    width=0.5)  # Band width of the bars

# Set the title and labels
plt.title('Average Monthly Temperatures', fontsize=16)
plt.ylabel('Temperature (°F)', fontsize=12)
plt.xlabel('Month', fontsize=12)

# Set y-axis limit to start from 30
plt.ylim(30, 90)

# Display the chart
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()