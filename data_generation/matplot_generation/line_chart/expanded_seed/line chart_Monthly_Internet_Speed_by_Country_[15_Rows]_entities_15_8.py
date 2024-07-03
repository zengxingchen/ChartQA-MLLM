
import matplotlib.pyplot as plt

# Data provided in the question
chart_data = [
    {'Month': 'January', 'USA (Mbps)': 150, 'South Korea (Mbps)': 200, 'Australia (Mbps)': 100, 'Germany (Mbps)': 120},
    {'Month': 'February', 'USA (Mbps)': 152, 'South Korea (Mbps)': 205, 'Australia (Mbps)': 102, 'Germany (Mbps)': 123},
    # ... (Include all the month data here)
    {'Month': 'March', 'USA (Mbps)': 178, 'South Korea (Mbps)': 270, 'Australia (Mbps)': 128, 'Germany (Mbps)': 155}
]

# Extracting the data for plotting
months = [entry['Month'] for entry in chart_data]
usa_speeds = [entry['USA (Mbps)'] for entry in chart_data]
south_korea_speeds = [entry['South Korea (Mbps)'] for entry in chart_data]
australia_speeds = [entry['Australia (Mbps)'] for entry in chart_data]
germany_speeds = [entry['Germany (Mbps)'] for entry in chart_data]

# Plotting the data
plt.figure(figsize=(10, 6))

plt.plot(months, usa_speeds, label='USA', marker='o', linestyle='-', color='blue')
plt.plot(months, south_korea_speeds, label='South Korea', marker='s', linestyle='--', color='red')
plt.plot(months, australia_speeds, label='Australia', marker='^', linestyle='-.', color='green')
plt.plot(months, germany_speeds, label='Germany', marker='d', linestyle=':', color='purple')

# Adding the title and labels
plt.title('Internet Speed by Country')
plt.xlabel('Month')
plt.ylabel('Speed (Mbps)')
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability

# Adding a legend
plt.legend()

# Adjust layout to prevent clipping and show the plot
plt.tight_layout()
plt.show()