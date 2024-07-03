
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
sales = [150, 120, 180, 160, 190, 175, 200, 210, 190, 170, 160, 180]

# Create a new figure with specific width and height
plt.figure(figsize=(16, 8))

# Plotting the line chart with a specific color scheme
plt.plot(months, sales, marker='o', linestyle='-', color='#1f77b4')  # Blue color

# Assign annotations/labels to specific data points to provide additional information
for i, sale in enumerate(sales):
    plt.annotate(str(sale), xy=(months[i], sale), xytext=(5, 5), textcoords='offset points')

# Modify the chart title and labels
plt.title('Monthly Sales Performance in a Retail Store', pad=20)
plt.xlabel('Month')
plt.ylabel('Sales ($1000)')

# Invert the y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()