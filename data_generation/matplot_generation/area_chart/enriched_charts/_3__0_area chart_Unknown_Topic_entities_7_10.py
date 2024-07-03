
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']

visitors = [1050, 980, 1150, 1230, 1100, 1175, 1250, 1280, 1210, 1350, 1420, 1500]

# Plotting the area chart
plt.figure(figsize=(14, 8))
plt.fill_between(months, visitors, color='#1f77b4')

# Adding labels and title
plt.title('Monthly Visitor Statistics of a Museum Over a Year', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Visitors')

# Customizing the grid
plt.grid(True, color='#e6e6e6', linestyle='-', linewidth=0.7, which='both')

# Adjusting the x-axis labels to fit properly
plt.xticks(rotation=45)

# Annotating the chart with text labels
for i, val in enumerate(visitors):
    plt.text(i, val + 20, str(val), ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()