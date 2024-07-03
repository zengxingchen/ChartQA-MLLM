
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Month': 'January', 'Espresso (units)': 350, 'Latte (units)': 200, 'Iced Coffee (units)': 150, 'Tea (units)': 100},
    {'Month': 'February', 'Espresso (units)': 400, 'Latte (units)': 250, 'Iced Coffee (units)': 100, 'Tea (units)': 150},
    {'Month': 'March', 'Espresso (units)': 450, 'Latte (units)': 300, 'Iced Coffee (units)': 120, 'Tea (units)': 160},
    {'Month': 'April', 'Espresso (units)': 420, 'Latte (units)': 330, 'Iced Coffee (units)': 130, 'Tea (units)': 170},
    {'Month': 'May', 'Espresso (units)': 480, 'Latte (units)': 350, 'Iced Coffee (units)': 140, 'Tea (units)': 180},
    {'Month': 'June', 'Espresso (units)': 500, 'Latte (units)': 370, 'Iced Coffee (units)': 300, 'Tea (units)': 190},
    {'Month': 'July', 'Espresso (units)': 520, 'Latte (units)': 390, 'Iced Coffee (units)': 310, 'Tea (units)': 200},
    {'Month': 'August', 'Espresso (units)': 540, 'Latte (units)': 410, 'Iced Coffee (units)': 320, 'Tea (units)': 190},
    {'Month': 'September', 'Espresso (units)': 530, 'Latte (units)': 400, 'Iced Coffee (units)': 300, 'Tea (units)': 180},
    {'Month': 'October', 'Espresso (units)': 490, 'Latte (units)': 370, 'Iced Coffee (units)': 290, 'Tea (units)': 170},
    {'Month': 'November', 'Espresso (units)': 470, 'Latte (units)': 340, 'Iced Coffee (units)': 200, 'Tea (units)': 160},
    {'Month': 'December', 'Espresso (units)': 600, 'Latte (units)': 450, 'Iced Coffee (units)': 210, 'Tea (units)': 200}
]

# Extracting data for plotting
months = [entry['Month'] for entry in data]
espresso_units = [entry['Espresso (units)'] for entry in data]
latte_units = [entry['Latte (units)'] for entry in data]
iced_coffee_units = [entry['Iced Coffee (units)'] for entry in data]
tea_units = [entry['Tea (units)'] for entry in data]

# Plotting the stacked area chart
fig, ax = plt.subplots()

ax.stackplot(months, espresso_units, latte_units, iced_coffee_units, tea_units, labels=['Espresso', 'Latte', 'Iced Coffee', 'Tea'],
             colors=['#1b9e77', '#d95f02', '#7570b3', '#e7298a'], alpha=0.5)

# Labeling the axes and the title
ax.set_xlabel('Month')
ax.set_ylabel('Units Sold')
ax.set_title('Monthly Sales Data - Stacked Area Chart')

# Adding a legend
ax.legend(loc='upper left')

# Rotating the x-axis labels for better readability
plt.xticks(rotation=45)

# Showing the plot
plt.tight_layout()
plt.show()