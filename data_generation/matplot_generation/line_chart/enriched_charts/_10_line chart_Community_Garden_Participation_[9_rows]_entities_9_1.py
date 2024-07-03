
import matplotlib.pyplot as plt

# Data provided in the table
data = [
    {'Month': 'January', 'Temperature (°C)': 5, 'Location': 'Mountain View'},
    {'Month': 'February', 'Temperature (°C)': 7, 'Location': 'Mountain View'},
    {'Month': 'March', 'Temperature (°C)': 12, 'Location': 'Mountain View'},
    {'Month': 'April', 'Temperature (°C)': 18, 'Location': 'Mountain View'},
    {'Month': 'May', 'Temperature (°C)': 23, 'Location': 'Mountain View'},
    {'Month': 'June', 'Temperature (°C)': 28, 'Location': 'Mountain View'},
    {'Month': 'July', 'Temperature (°C)': 35, 'Location': 'Mountain View'},
    {'Month': 'August', 'Temperature (°C)': 33, 'Location': 'Mountain View'},
    {'Month': 'September', 'Temperature (°C)': 27, 'Location': 'Mountain View'},
    {'Month': 'October', 'Temperature (°C)': 20, 'Location': 'Mountain View'},
    {'Month': 'November', 'Temperature (°C)': 12, 'Location': 'Mountain View'},
    {'Month': 'December', 'Temperature (°C)': 6, 'Location': 'Mountain View'}
]

# Extracting the months and the temperatures
months = [entry['Month'] for entry in data]
temperatures = [entry['Temperature (°C)'] for entry in data]

# Creating the line chart
plt.figure(figsize=(12, 7))  # Setting the figure size

# Plotting the data with various visual encodings
plt.plot(months, temperatures, color='#1f77b4', linestyle='-', linewidth=2, 
         marker='o', markersize=8, markerfacecolor='#ff7f0e', markeredgewidth=2, 
         markeredgecolor='#d62728', label='Temperature at Mountain View')

# Adding titles and labels
plt.title('Monthly Average Temperature at Mountain View', fontsize=16, loc='left')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)

# Adding a legend
plt.legend(loc='upper right')

# Adding a grid
plt.grid(True)

# Adding customization with font size and style for x and y ticks
plt.xticks(fontsize=10, fontweight='bold', rotation=45)
plt.yticks(fontsize=10, fontweight='bold')

# Adding annotations for specific points
plt.annotate('Peak Temperature', xy=('July', 35), xytext=('May', 35),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='green')

# Show plot
plt.show()