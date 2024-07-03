
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']

kWh = [350, 320, 290, 280, 300, 275, 260, 270, 280, 310, 330, 360]

# Plotting the area chart
plt.figure(figsize=(12, 6))
plt.fill_between(months, kWh, color='#ff7f0e')

# Adding labels and title
plt.title('Monthly Electricity Consumption of a Household Over a Year')
plt.xlabel('Month')
plt.ylabel('Electricity Consumption (kWh)')

# Customizing the grid
plt.grid(True, color='#e6e6e6', linestyle='-', linewidth=0.7, which='both')

# Adjusting the x-axis labels to fit properly
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()