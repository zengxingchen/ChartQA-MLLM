
import matplotlib.pyplot as plt

# Data provided in the table
data = [
    {'Month': 'January', 'CO2 Emissions (Metric Tons)': 4.5, 'Location': 'Mountain View'},
    {'Month': 'February', 'CO2 Emissions (Metric Tons)': 5.2, 'Location': 'Mountain View'},
    {'Month': 'March', 'CO2 Emissions (Metric Tons)': 5.8, 'Location': 'Mountain View'},
    {'Month': 'April', 'CO2 Emissions (Metric Tons)': 6.5, 'Location': 'Mountain View'},
    {'Month': 'May', 'CO2 Emissions (Metric Tons)': 7.1, 'Location': 'Mountain View'},
    {'Month': 'June', 'CO2 Emissions (Metric Tons)': 7.8, 'Location': 'Mountain View'},
    {'Month': 'July', 'CO2 Emissions (Metric Tons)': 8.4, 'Location': 'Mountain View'},
    {'Month': 'August', 'CO2 Emissions (Metric Tons)': 8.1, 'Location': 'Mountain View'},
    {'Month': 'September', 'CO2 Emissions (Metric Tons)': 7.3, 'Location': 'Mountain View'},
    {'Month': 'October', 'CO2 Emissions (Metric Tons)': 6.7, 'Location': 'Mountain View'},
    {'Month': 'November', 'CO2 Emissions (Metric Tons)': 5.9, 'Location': 'Mountain View'},
    {'Month': 'December', 'CO2 Emissions (Metric Tons)': 4.8, 'Location': 'Mountain View'}
]

# Extracting the months and the CO2 emissions
months = [entry['Month'] for entry in data]
emissions = [entry['CO2 Emissions (Metric Tons)'] for entry in data]

# Creating the line chart
plt.figure(figsize=(14, 8))  # Setting the figure size

# Plotting the data with various visual encodings
plt.plot(months, emissions, color='#2ca02c', linestyle='-', linewidth=2, 
         marker='s', markersize=8, markerfacecolor='#ff9896', markeredgewidth=2, 
         markeredgecolor='#8c564b', label='CO2 Emissions in Mountain View')

# Adding titles and labels
plt.title('Monthly CO2 Emissions in Mountain View', fontsize=18, loc='center')
plt.xlabel('Month', fontsize=14)
plt.ylabel('CO2 Emissions (Metric Tons)', fontsize=14)

# Adding a legend
plt.legend(loc='upper left')

# Adding a grid
plt.grid(True)

# Adding customization with font size and style for x and y ticks
plt.xticks(fontsize=12, fontweight='bold', rotation=45)
plt.yticks(fontsize=12, fontweight='bold')

# Adding annotations for specific points
plt.annotate('Highest Emissions', xy=('July', 8.4), xytext=('May', 9),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='red')

# Show plot
plt.show()