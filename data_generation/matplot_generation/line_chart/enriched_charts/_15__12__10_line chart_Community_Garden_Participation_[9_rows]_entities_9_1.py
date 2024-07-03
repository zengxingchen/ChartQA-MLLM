
import matplotlib.pyplot as plt

# Data provided in the table
data = [
    {'Month': 'January', 'CO2 Emissions (Metric Tons)': 8.4, 'Location': 'Mountain View'},
    {'Month': 'February', 'CO2 Emissions (Metric Tons)': 7.9, 'Location': 'Mountain View'},
    {'Month': 'March', 'CO2 Emissions (Metric Tons)': 7.3, 'Location': 'Mountain View'},
    {'Month': 'April', 'CO2 Emissions (Metric Tons)': 6.7, 'Location': 'Mountain View'},
    {'Month': 'May', 'CO2 Emissions (Metric Tons)': 6.0, 'Location': 'Mountain View'},
    {'Month': 'June', 'CO2 Emissions (Metric Tons)': 5.3, 'Location': 'Mountain View'},
    {'Month': 'July', 'CO2 Emissions (Metric Tons)': 4.7, 'Location': 'Mountain View'},
    {'Month': 'August', 'CO2 Emissions (Metric Tons)': 4.3, 'Location': 'Mountain View'},
    {'Month': 'September', 'CO2 Emissions (Metric Tons)': 4.1, 'Location': 'Mountain View'},
    {'Month': 'October', 'CO2 Emissions (Metric Tons)': 4.0, 'Location': 'Mountain View'},
    {'Month': 'November', 'CO2 Emissions (Metric Tons)': 4.1, 'Location': 'Mountain View'},
    {'Month': 'December', 'CO2 Emissions (Metric Tons)': 4.3, 'Location': 'Mountain View'}
]

# Extracting the months and the CO2 emissions
months = [entry['Month'] for entry in data]
emissions = [entry['CO2 Emissions (Metric Tons)'] for entry in data]

# Creating the line chart
plt.figure(figsize=(16, 10))  # Setting the figure size

# Plotting the data with various visual encodings
plt.plot(months, emissions, color='#1f77b4', linestyle='-', linewidth=3, 
         marker='o', markersize=10, markerfacecolor='#ff7f0e', markeredgewidth=2, 
         markeredgecolor='#d62728', label='CO2 Emissions in Mountain View')

# Adding titles and labels
plt.title('Monthly CO2 Emissions in Mountain View (Reversed)', fontsize=20, loc='center')
plt.xlabel('Month', fontsize=16)
plt.ylabel('CO2 Emissions (Metric Tons)', fontsize=16)

# Adding a legend
plt.legend(loc='upper right')

# Adding a grid
plt.grid(True)

# Adding customization with font size and style for x and y ticks
plt.xticks(fontsize=14, fontweight='bold', rotation=45)
plt.yticks(fontsize=14, fontweight='bold')

# Adding annotations for specific points
plt.annotate('Highest Emissions', xy=('January', 8.4), xytext=('March', 9),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=14, color='green')

# Invert the y-axis
plt.gca().invert_yaxis()

# Show plot
plt.show()