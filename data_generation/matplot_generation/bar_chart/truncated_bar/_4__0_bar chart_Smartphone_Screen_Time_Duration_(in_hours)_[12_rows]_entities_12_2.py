
import matplotlib.pyplot as plt

# Data to plot
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [210, 230, 250, 270, 290, 310, 330, 350, 370, 390, 410, 430]

# Plot a vertical bar chart
plt.figure(figsize=(12, 6))  # Width and height of the chart
plt.bar(x=months, height=temperatures, color=[
    '#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', 
    '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', 
    '#BCBD22', '#17BECF', '#AEC7E8', '#FFBB78'], 
    width=0.4)  # Width of the bars

# Set the title and labels
plt.title('Monthly Temperature Data for the Year', fontsize=16)
plt.ylabel('Temperature (in °C)', fontsize=12)
plt.xlabel('Month', fontsize=12)

# Set y-axis limits to create a truncated chart
plt.ylim(100, 500)

# Display the chart
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()