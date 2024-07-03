
import matplotlib.pyplot as plt

# Data
months = [
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
]
temperatures = [5, 7, 10, 15, 20, 25, 30, 28, 22, 16, 10, 6]

# Plotting the bar chart
plt.figure(figsize=(12, 7))  # changing width and height of the chart
plt.bar(months, temperatures, width=0.6, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33FB', 
    '#57FF33', '#FFDA33', '#FF335E', '#33FFF6', 
    '#8B33FF', '#33FFB2', '#DAFF33', '#FF8333'
])  # change direction and color scheme of bars

# Customizing the plot
plt.ylabel('Temperature in Celsius')  # changing chart headline
plt.title('Monthly Average Temperature')  # changing topic
plt.ylim(0, 35)  # adjust the limit to better spread out the bars

# Show the plot
plt.show()