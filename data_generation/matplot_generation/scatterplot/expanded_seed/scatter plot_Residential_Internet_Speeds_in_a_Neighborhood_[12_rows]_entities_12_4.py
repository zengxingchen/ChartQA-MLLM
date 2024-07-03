
import matplotlib.pyplot as plt

# Your provided data
data = [
    {'House Number': 1, 'Internet Speed (Mbps)': 50, 'Monthly Price ($)': 40},
    {'House Number': 2, 'Internet Speed (Mbps)': 100, 'Monthly Price ($)': 60},
    {'House Number': 3, 'Internet Speed (Mbps)': 75, 'Monthly Price ($)': 50},
    {'House Number': 4, 'Internet Speed (Mbps)': 20, 'Monthly Price ($)': 30},
    {'House Number': 5, 'Internet Speed (Mbps)': 50, 'Monthly Price ($)': 45},
    {'House Number': 6, 'Internet Speed (Mbps)': 150, 'Monthly Price ($)': 80},
    {'House Number': 7, 'Internet Speed (Mbps)': 120, 'Monthly Price ($)': 70},
    {'House Number': 8, 'Internet Speed (Mbps)': 100, 'Monthly Price ($)': 65},
    {'House Number': 9, 'Internet Speed (Mbps)': 75, 'Monthly Price ($)': 55},
    {'House Number': 10, 'Internet Speed (Mbps)': 200, 'Monthly Price ($)': 99},
    {'House Number': 11, 'Internet Speed (Mbps)': 50, 'Monthly Price ($)': 42},
    {'House Number': 12, 'Internet Speed (Mbps)': 150, 'Monthly Price ($)': 85}
]

# Extracting house numbers, internet speeds and monthly prices for plotting
house_numbers = [item['House Number'] for item in data]
internet_speeds = [item['Internet Speed (Mbps)'] for item in data]
monthly_prices = [item['Monthly Price ($)'] for item in data]

# Define the size of each point based on internet speed
sizes = [speed / 200 * 100 for speed in internet_speeds]  # Normalize the speed for point size

# Choose a color for each point based on its monthly price
colors = monthly_prices

# Create a scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(house_numbers, internet_speeds, s=sizes, c=colors, cmap='viridis', alpha=0.6, edgecolors='w', linewidth=1)

# Add a color bar
plt.colorbar(scatter)

# Set plot title and labels
plt.title('Internet Speed and Monthly Price per House')
plt.xlabel('House Number')
plt.ylabel('Internet Speed (Mbps)')

# Add grid lines for better readability
plt.grid(True)

# Show the scatter plot
plt.show()