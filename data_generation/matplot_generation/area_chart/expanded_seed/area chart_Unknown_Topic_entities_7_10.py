
import matplotlib.pyplot as plt

# Data
data = [{'Month': 'January', 'Rainfall (mm)': 79}, {'Month': 'February', 'Rainfall (mm)': 52},
        {'Month': 'March', 'Rainfall (mm)': 64}, {'Month': 'April', 'Rainfall (mm)': 87},
        {'Month': 'May', 'Rainfall (mm)': 103}, {'Month': 'June', 'Rainfall (mm)': 29},
        {'Month': 'July', 'Rainfall (mm)': 58}]

# Extracting data for the area chart
months = [entry['Month'] for entry in data]
rainfall = [entry['Rainfall (mm)'] for entry in data]

# Plotting
plt.fill_between(months, rainfall, color="skyblue", alpha=0.4)
plt.plot(months, rainfall, color="Slateblue", alpha=0.6, linewidth=2)

# Customizing the plot with diversified visual encodings
plt.xticks(rotation=45)                       # Rotate x-axis labels for better readability
plt.yticks(range(0, max(rainfall)+50, 10))    # Set y-axis ticks to cover the range of data
plt.xlabel('Month')                           # X-axis label
plt.ylabel('Rainfall (mm)')                   # Y-axis label
plt.title('Monthly Rainfall')                 # Chart title
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.5)  # Adding a grid
plt.tight_layout()                            # Automatically adjust subplot params for the plot to fit into the figure area.

# Show the plot
plt.show()