
import matplotlib.pyplot as plt

# Given table data
data = [
    {'Month': 'January', 'Espresso Drinks': 1200, 'Brewed Coffee': 900, 'Pastries': 450, 'Teas': 300},
    {'Month': 'February', 'Espresso Drinks': 1100, 'Brewed Coffee': 950, 'Pastries': 420, 'Teas': 320},
    {'Month': 'March', 'Espresso Drinks': 1500, 'Brewed Coffee': 1000, 'Pastries': 500, 'Teas': 350},
    {'Month': 'April', 'Espresso Drinks': 1600, 'Brewed Coffee': 1100, 'Pastries': 520, 'Teas': 370}
]

# Extracting month labels for the x-axis
months = [item['Month'] for item in data]

# Values for each category
espresso_drinks = [item['Espresso Drinks'] for item in data]
brewed_coffee = [item['Brewed Coffee'] for item in data]
pastries = [item['Pastries'] for item in data]
teas = [item['Teas'] for item in data]

# Placing the x-axis positions
x_positions = range(len(months))

# Plotting each category as a part of the stack
plt.bar(x_positions, espresso_drinks, label='Espresso Drinks', color='brown')
plt.bar(x_positions, brewed_coffee, label='Brewed Coffee', bottom=espresso_drinks, color='black')
plt.bar(x_positions, pastries, label='Pastries', bottom=[i+j for i,j in zip(espresso_drinks, brewed_coffee)], color='tan')
plt.bar(x_positions, teas, label='Teas', bottom=[i+j+k for i,j,k in zip(espresso_drinks, brewed_coffee, pastries)], color='green')

# Adding axis labels and chart title
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Coffee Shop Sales Data')

# Adding month labels to x-axis
plt.xticks(x_positions, months)

# Adding a legend
plt.legend(loc='upper left')

# Display the plot
plt.show()