
import matplotlib.pyplot as plt

# Data
months = [
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
]
sales = [200, 210, 190, 220, 230, 210, 240, 230, 220, 215, 225, 235]

# Plotting the bar chart
plt.figure(figsize=(10, 8))  # changing width and height of the chart
plt.barh(months, sales, height=0.5, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33FB', 
    '#57FF33', '#FFDA33', '#FF335E', '#33FFF6', 
    '#8B33FF', '#33FFB2', '#DAFF33', '#FF8333'
])  # change direction and color scheme of bars

# Customizing the plot
plt.xlabel('Sales in USD')  # changing chart headline
plt.title('Monthly Sales Data')  # changing topic
plt.xlim(150, 250)  # adjust the limit to better spread out the bars

# Show the plot
plt.show()