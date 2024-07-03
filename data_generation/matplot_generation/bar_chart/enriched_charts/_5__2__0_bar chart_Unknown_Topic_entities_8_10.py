
import matplotlib.pyplot as plt

# Data
events = [
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
]
sales = [250, 220, 280, 300, 270, 320, 310, 330, 300, 290, 310, 350]

# Plotting the bar chart
plt.figure(figsize=(14, 8))
plt.barh(events, sales, height=0.6, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', 
    '#A133FF', '#33FFF5', '#FF8C33', '#8C33FF', 
    '#FF3333', '#33FFA1', '#F5FF33', '#5733FF'
])

# Customizing the plot
plt.xlabel('Sales (in $1000s)')
plt.title('Monthly Sales Statistics')
plt.xlim(200, 360)

# Show the plot
plt.show()